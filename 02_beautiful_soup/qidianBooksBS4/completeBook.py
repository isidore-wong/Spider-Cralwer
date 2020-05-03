# _*_ coding:utf-8 _*_

from bs4 import BeautifulSoup
import urllib.request
import re
import codecs
import time
from mylog import MyLog as mylog
from save2mysql import SavebooksData


"""
@author: Isidore
@email:616132717@qq.com
@file: completeBook.py
@time: 2018/12/16  21:40
@version: 1.0
"""

"""
程序目的：从起点小说网上爬取完本的小说名单
"""


class BookItem(object):
    categoryName = None
    bookName = None
    wordsNum = None
    authorName = None


class GetBookName(object):
    def __init__(self):
        self.urlBase = 'https://www.qidian.com/all?action=1&orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1'
        self.log = mylog()
        self.pages = self.getPages(self.urlBase)
        self.booksList = []
        # self.spider(self.urlBase, 5)
        self.spider(self.urlBase, self.pages)
        self.pipelines(self.booksList)
        self.log.info('begin save data to mysql\r\n')
        SavebooksData(self.booksList)
        self.log.info('save data to mysql end ...\r\n')

    def getPages(self, url):
        '''获取总页数 '''
        htmlContent = self.getResponseContent(url)
        pattern = re.compile('data-pageMax=".*?"')
        pageStr = pattern.search(htmlContent).group()
        pageMax = pageStr.split('"')[1]
        print("pageMax = %s" % pageMax)
        return int(pageMax)

    def getResponseContent(self, url):
        try:
            response = urllib.request.urlopen(url, timeout=3)
        except:
            self.log.error('Python 返回URL:%s  数据失败' % url)
            return None
        else:
            self.log.info('Python 返回URU:%s  数据成功' % url)
            return response.read().decode('utf-8')

    def spider(self, url, pages):
        urlList = url.split('=')
        # page_num = 60
        page_num = 10
        for i in range(1, page_num + 1):
            urlList[-1] = str(i)
            newUrl = '='.join(urlList)
            htmlContent = self.getResponseContent(newUrl)
            if not htmlContent:
                self.mylog.error('未获取到页面内容')
                continue
            soup = BeautifulSoup(htmlContent, 'lxml')
            tags = soup.find_all('li', attrs={'data-rid': re.compile('\d{1,2}')})
            for tag in tags:
                item = BookItem()
                item.categoryName = tag.find('a', attrs={'class': 'go-sub-type'}).get_text()
                # item.middleUrl = tag.find('h4').a.get('href')
                item.bookName = tag.find('h4').a.get_text()
                item.wordsNum = tag.find_all(re.compile('span'))[-1].get_text()
                # item.updateTime = None
                item.authorName = tag.find('a', attrs={'class': 'name'}).get_text()
                self.booksList.append(item)
                self.log.info('获取书名为<<%s>>的数据成功' % item.bookName)

    def pipelines(self, bookList):
        bookName = '起点完本小说.txt'
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S\r\n', time.localtime())
        with codecs.open(bookName, 'w', 'utf8') as fp:
            fp.write('run time: %s' % nowTime)
            for item in self.booksList:
                fp.write('%s \t %s \t\t %s \t  %s \r\n'
                         % (item.categoryName, item.bookName, item.wordsNum, item.authorName))
                self.log.info('将书名为<<%s>>的数据存入"%s"...' % (item.bookName, bookName))


if __name__ == '__main__':
    GBN = GetBookName()
