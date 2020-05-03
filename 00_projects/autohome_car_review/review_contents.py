#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import codecs
import time
from mylog import MyLog as mylog
from save2sql import SaveReviewData

"""
@version: 1.0
@author: isidore wong
@contact: isidore_wong@163.com
@site: https://github.com/isidore-wong
@file: review_contents.py
@time: 2019/9/5 11:43
"""

"""
program purpose: for mining the evaluation of car,  we crawl the review information 
from vertical website forums
"""


class ReviewItem(object):
    postID = None
    postName = None
    pubTime = None
    postUrl = None

class GetReviewData(object):
    def __init__(self):
        self.urlBase = 'https://k.autohome.com.cn/448/12433/index_1.html?GradeEnum=0#dataList'
        self.log = mylog()
        self.pages = self.getPages(self.urlBase)
        self.reviewList = []
        self.spider(self.urlBase, self.pages)
        self.pipeline(self.reviewList)
        self.log.info('review url is beginning to save into mysql\r\n')
        self.SaveReviewData(self.reviewList)
        self.log.info('saving data into mysql is end\r\n')

    def getPages(self, url):
        # get totoal pages
        htmlContent = self.getResponseContent(url)




    def getResponseContent(self, url):
        pass

    def spider(self, url, pages):
        pass

    def pipeline(self, reviewlist):
        pass



    



