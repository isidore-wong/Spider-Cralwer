# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
import re
import time
import codecs
from mylog import Mylog as mylog
from review_sql import SaveReviewUrlData

"""
@version: python 3.6
@author: Isidore
@contact: 616132717@qq.com
@time: 2019/09/10 21:41
"""

"""
程序目的：
获取汽车之家口碑帖信息，对采集到的数据进行文本分析等。采集的信息包含三部分评论内容：
1.结构类数据：空间、动力等评分数据
2.半结构化数据：购买车型、购车目的等数据
3.文本类数据：最满意、最不满意等文本数据

程序实施步骤：
1.从口碑列表页获取评论的页数和口碑内容部分的URL
2.根据口碑内容URL获取以上的三部分评论数据
3.根据采集到的的数据进行文本分析
"""

class GetReviewUrl(object):
    def __init__(self):
        self.startUrl = "https://k.autohome.com.cn/448/12433/#pvareaid=3454474"
        self.log = mylog()
        self.pageNum = self.getPage(self.startUrl)
        self.urlList = []
        self.spider(self.startUrl, self.pageNum)
        self.pipelines(self.urlList)
        self.log.into("begin to save url to review_url_tb\r\n")
        SaveReviewUrlData(self.urlList)
        self.log.into("saving url to review_url_tb is end\r\n")


    def getPage(self, url):
        '''get max pages of review list'''
        res_content = self.getResponseContent(url)
        soup = BeautifulSoup(res_content, 'lxml')
        page_str = soup.find("span", attrs={"class":"page-item-info"}).get_text()
        page_num = page_str.re.compile(r'/d+')
        return page_num


    def getResponseContent(self, url):
        header = {
            "Host": "autohome.com.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "h-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        try:
            response = requests.get(url, headers=header, timeout=3)
        except:
            self.log.error("data<%s> getted is failure" % url)
            return None
        else:
            self.log.info("data<%s> getted is successful" % url)
            return response.text


    def spider(self, startUrl, num):
       # url_list = []
        for i in range(num):
            url_spider = "https://k.autohome.com.cn/448/12433/index_"+ str(i) +".html?GradeEnum=0#dataList"
            htmlContent = self.getResponseContent(url_spider)
            if not htmlContent:
                self.log.error("Page content not fetched")
                continue
            soup = BeautifulSoup(htmlContent, 'lxml')
            url = soup.find("a", attrs={'class':'btn btn-small fn-left'}).get('href')
            self.urlList.append(url)
            self.log.info("review url <%s> getted is successful" % url)


    def pipelines(self, urlList):
        urlName = "AutohomeUrlList.txt"
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S\r\n", time.localtime())
        with codecs.open(urlName, 'w', 'utf8') as fp:
            fp.write("run time: %s" % nowTime)
            for item in urlList:
                fp.write("%s\r\n" % item.content_url)
            self.log.info("save review url <%s> into %s..." % (item.content_url, urlName))











