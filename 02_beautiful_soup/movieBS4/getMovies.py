# _*_ coding:utf-8 _*_
import codecs
import re
from bs4 import BeautifulSoup
import time
import urllib.request
from mylog import MyLog as mylog


"""
@author: Isidore
@email:616132717@qq.com
@file: getMovies.py
@time: 2018/12/24  16:20
@version:1.0
"""

"""
程序目的：爬取电影网站的电影信息
"""


class MovieItem(object):
    # 根据要爬取的信息定义变量
    movie_name = None
    movie_score = None
    movie_star = None


class GetMovie(object):
    # 获取电影信息
    def __init__(self):
        self.urlBase = 'http://dianying.2345.com/list/----2018---1.html'
        self.log = mylog()
        self.urls = []
        self.items = []
        self.pages = self.getPages()
        self.getUrls(self.pages)
        self.spider(self.urls)
        self.pipeline(self.items)

    def getPages(self):
        # 获取总页数
        self.log.info('开始获取页数')
        html_content = self.getResponseContent(self.urlBase)
        soup = BeautifulSoup(html_content, 'lxml')
        tag = soup.find('div', attrs={'class': 'v_page'}).get_text()
        pages = str(tag[-7] + tag[-6])
        self.log.info('获取页数成功')
        return int(pages)

    def getUrls(self, pages):
        url_head = 'http://dianying.2345.com/list/----2018---'
        url_end = '.html'
        for i in range(1, pages + 1):
            url = url_head + str(i) + url_end
            self.urls.append(url)
            self.log.info('添加{url}到urls列表中'.format(url=url))

    def spider(self, urls):
        for url in urls:
            html_content = self.getResponseContent(url)
            soup = BeautifulSoup(html_content, 'lxml')
            anchor_tag = soup.find('ul', attrs={'class': 'v_picTxt pic180_240 clearfix'})
            tags = anchor_tag.find_all('li', attrs={'media': re.compile(r'\d{6}')})
            for tag in tags:
                item = MovieItem()
                item.movie_name = tag.find('span', attrs={'class': 'sTit'}).get_text()
                item.movie_score = tag.find('span', attrs={'class': 'pRightBottom'}).em.get_text().replace('分', '')
                item.movie_star = tag.find('span', attrs={'class': 'sDes'}).get_text().replace('主演: ', '')
                self.items.append(item)
                self.log.info('获取电影名为：%s成功' % (item.movie_name))

    def pipeline(self, items):
        file_name = '2018年热门电影.txt'
        with codecs.open(file_name, 'w', 'utf-8') as fp:
            for item in items:
                fp.write('%s \t %s \t %s \r\n' % (item.movie_name, item.movie_score, item.movie_star))
                self.log.info(
                    '电影名：《%s》已成功存入文件"%s"中...' %
                    (item.movie_name, file_name))

    def getResponseContent(self, url):
        fakeHeaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'}
        request = urllib.request.Request(url, headers=fakeHeaders)
        try:
            response = urllib.request.urlopen(request)
        except BaseException:
            self.log.error('Python 返回URL:%s  数据失败' % url)
            return None
        else:
            self.log.info('Python 返回URL:%s  数据成功' % url)
            return response.read().decode('GBK')


if __name__ == '__main__':
    GM = GetMovie()
