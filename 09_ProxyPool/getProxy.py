# --*-- coding:utf-8 --*--

'''
@File: getProxy.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-12-16 10:43
'''

'''
在这里实现了几个示例，如抓取代理 66、Proxy360、Goubanjia 三个免费代理网站，这些方法都定义成了生成器，
通过 yield 返回一个个代理。程序首先获取网页，然后用 pyquery 解析，解析出 IP 加端口的形式的代理然后返回。

然后定义了一个 get_proxies() 方法，将所有以 crawl 开头的方法调用一遍，获取每个方法返回的代理并组合成列表形式返回。

你可能会想知道，如何获取所有以 crawl 开头的方法名称呢？其实这里借助了元类来实现。我们定义了一个 
ProxyMetaclass，Crawler 类将它设置为元类，元类中实现了 __new__() 方法，这个方法有固定的几个参数，
第四个参数 attrs 中包含了类的一些属性。我们可以遍历 attrs 这个参数即可获取类的所有方法信息，就像遍历字典一样，
键名对应方法的名称。然后判断方法的开头是否 crawl，如果是，则将其加入到 __CrawlFunc__属性中。
这样我们就成功将所有以 crawl 开头的方法定义成了一个属性，动态获取到所有以 crawl 开头的方法列表。

所以，如果要做扩展，我们只需要添加一个以 crawl 开头的方法。例如抓取快代理，我们只需要在 Crawler 类中增加
crawl_kuaidaili() 方法，仿照其他几个方法将其定义成生成器，抓取其网站的代理，然后通过 yield 返回代理即可。
这样，我们可以非常方便地扩展，而不用关心类其他部分的实现逻辑。
'''

import json
from .utils import get_page
from pyquery import PyQuery as pq

class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)

class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print(' 成功获取到代理 ', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=4):
        """
        获取代理 66
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_proxy360(self):
        """
        获取 Proxy360
        :return: 代理
        """
        start_url = 'http://www.proxy360.cn/Region/China'
        print('Crawling', start_url)
        html = get_page(start_url)
        if html:
            doc = pq(html)
            lines = doc('div[name="list_proxy_ip"]').items()
            for line in lines:
                ip = line.find('.tbBottomLine:nth-child(1)').text()
                port = line.find('.tbBottomLine:nth-child(2)').text()
                yield ':'.join([ip, port])

    def crawl_goubanjia(self):
        """
        获取 Goubanjia
        :return: 代理
        """
        start_url = 'http://www.goubanjia.com/free/gngn/index.shtml'
        html = get_page(start_url)
        if html:
            doc = pq(html)
            tds = doc('td.ip').items()
            for td in tds:
                td.find('p').remove()
                yield td.text().replace(' ', '')
