# _*_ coding:utf-8 _*_
import urllib.request
import codecs
import re
from bs4 import BeautifulSoup
from save2excel import SaveBallData
from mylog import MyLog as mylog


"""
@author: Isidore
@email:616132717@qq.com
@file: getWinningNum.py
@time: 2018/12/23  16:18
@version: 1.0
"""

"""
程序目的：爬取双色球开奖数据并存储到Excel中
"""


class DoubleColorBallItem(object):
    # 定义所需的变量
    date = None
    order = None
    red1 = None
    red2 = None
    red3 = None
    red4 = None
    red5 = None
    red6 = None
    blue = None
    money = None
    firstPrize = None
    secondPrize = None


class GetDoubleColorBallNumber(object):
    # 获取双色球的开奖信息，并返回至一个txt文件中
    def __init__(self):
        self.urls = []
        self.log = mylog()
        self.getUrls()
        self.items = self.spider(self.urls)
        self.pipeline(self.items)
        self.log.info('begin saving data to excel \r\n')
        SaveBallData(self.items)
        self.log.info('end saving data to excel \r\n')

    def getUrls(self):
        # 获取数据来源的网页链接
        URL = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
        html_content = self.getResponseContent(URL)
        soup = BeautifulSoup(html_content, 'lxml')
        tag = soup.find_all(re.compile('p'))[-1]
        page_num = range(1, 16)
        for i in page_num:
            url = r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' + \
                str(i) + '.html'
            self.urls.append(url)
            self.log.info('添加URL:%s 到URLS \r\n' % url)

    def getResponseContent(self, url):
        # 获取网页内容单独使用一个函数，为了方便后续加入headers和proxy等内容
        try:
            response = urllib.request.urlopen(url)
        except BaseException:
            self.log.error('爬虫返回URL:%s 数据失败 \r\n' % url)
        else:
            self.log.info('爬虫返回URL:%s 数据成功 \r\n' % url)
            return response.read()

    def spider(self, urls):
        # 解析爬取到的网页内容，将开奖信息过滤出来
        items = []
        for url in urls:
            html_content = urllib.request.urlopen(url)
            soup = BeautifulSoup(html_content, 'lxml')
            tags = soup.find_all('tr', attrs={})
            for tag in tags:
                if tag.find('em'):
                    item = DoubleColorBallItem()
                    tag_td = tag.find_all('td')
                    item.date = tag_td[0].get_text()
                    item.order = tag_td[1].get_text()
                    tag_em = tag_td[2].find_all('em')
                    item.red1 = tag_em[0].get_text()
                    item.red2 = tag_em[1].get_text()
                    item.red3 = tag_em[2].get_text()
                    item.red4 = tag_em[3].get_text()
                    item.red5 = tag_em[4].get_text()
                    item.red6 = tag_em[5].get_text()
                    item.blue = tag_em[6].get_text()
                    item.money = tag_td[3].find('strong').get_text()
                    item.firstPrize = tag_td[4].find('strong').get_text()
                    item.secondPrize = tag_td[5].find('strong').get_text()
                    items.append(item)
                    self.log.info('获取日期为:%s 的数据成功' % (item.date))
        return items




    def pipeline(self, items):
        file_name = 'DoubleColorBall_data'
        with codecs.open(file_name, 'w', 'utf-8') as fp:
            for item in items:
                fp.write('%s %s \t %s %s %s %s %s %s  %s \t %s \t %s %s \r\n'
                      %(item.date,item.order,item.red1,item.red2,item.red3,item.red4,item.red5,item.red6,item.blue,item.money,item.firstPrize,item.secondPrize))
                self.log.info('将日期为:%s 的数据存入"%s"...' %(item.date, file_name))


if __name__ == '__main__':
    GDCBN = GetDoubleColorBallNumber()
