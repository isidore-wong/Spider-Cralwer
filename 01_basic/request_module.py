# _*_ coding:utf-8 _*_
import requests
import re
import urllib.request


"""
@version: python 3.6
@author: Isidore
@contact: 616132717@qq.com
@file: request_module.py
@time: 2018/11/09  14:58
"""

"""
程序目的：
学习requests库的基本用法
"""

# 通过re.sub()实现翻页功能

'''
def get_url():
    old_url = 'https://www.jikexueyuan.com/course/android/?pageNum=1'
    total_page = 11

    for i in range(1, total_page+1):
        new_link = re.sub('pageNum=\d+', 'pageNum=%d' % i, old_url, re.S)
        print(new_link)
'''


response = urllib.request.urlopen('http://www.58pic.com/').read()
print(response)


'''
if __name__ == '__main__':
    get_url()
'''
