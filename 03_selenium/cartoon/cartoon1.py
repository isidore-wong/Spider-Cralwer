# _*_ coding:utf-8 _*_

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from mylog import MyLog as mylog
import time
import os
import sys

"""
@author: Isidore
@email:616132717@qq.com
@file: cartoon1.py
@time: 2019/01/13  14:58
@version: 1.0
"""

"""
程序目的：采用selenium库中的webdriver抓取数据,
由于selenium与PhantomJS的分手，后采用Chrome/Firefox的headless方式抓取
"""


class GetCartoon(object):
    def __init__(self):
        self.startUrl = 'http://www.1kkk.com/ch1-406302/'
        self.log = mylog()
        self.browser = self.getBrowser()
        self.saveCartoon(self.browser)
        self.browser.quit()

    def getBrowser(self):

        # 最初采用PhantomJS进行动态抓取，由于PhantomJS被
        # browser = webdriver.PhantomJS(executable_path='E:/Learning/03-Programme/Python/script-libs/
        # phantomjs-2.1.1-windows/bin/phantomjs.exe')
        chrome_options = Options()

        # 此处由于set_headless属性的被遗弃，采用option的实例化方式进行
        chrome_options.headless = True
        chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(chrome_options=chrome_options)

        try:
            browser.get(self.startUrl)
        except Exception as e:
            mylog.error(
                'open the %s failed, exit the script ...' %
                self.startUrl)
            sys.exit(-1)

        browser.implicitly_wait(20)
        return browser

    def saveCartoon(self, browser):
        cartoonTitle = browser.title.split('_')[0]
        self.createDir(cartoonTitle)
        os.chdir(cartoonTitle)
        sumPage = int(self.browser.find_element_by_xpath('//*[@id="chapterpager"]/a[8]').text)
        i = 1
        while i <= sumPage:
            imgName = str(i) + '.png'
            browser.get_screenshot_as_file(imgName)


            self.log.info('save img %s' % imgName)
            i += 1
            NextTag = browser.find_element_by_xpath('/html/body/div[8]/div/a[2]')
            NextTag.click()
            #            browser.implicitly_wait(20)
            time.sleep(5)
        self.log.info('save img sccess')

    def createDir(self, dirName):
        if os.path.exists(dirName):
            self.log.error(
                'create directory %s failed, hava a same name file or directory' %
                dirName)
        else:
            try:
                os.makedirs(dirName)
            except BaseException:
                self.log.error('create directory %s failed' % dirName)
            else:
                self.log.info('create directory %s success' % dirName)


if __name__ == '__main__':
    GC = GetCartoon()
