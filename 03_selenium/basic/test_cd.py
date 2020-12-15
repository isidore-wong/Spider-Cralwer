# --*-- coding:utf-8 --*--
from selenium import webdriver

'''
@File: test_cd.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-12-14 9:16
'''

driver_path = 'D:/anaconda/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://www.baidu.com')
print(driver.page_source)