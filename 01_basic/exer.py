# _*_ coding:utf-8 _*_
import re
import urllib.request
from bs4 import BeautifulSoup
import codecs

"""
@version: python 3.6
@author: Isidore
@file: exer.py
@time: 2018/11/13  23:53
"""


URL = 'http://dianying.2345.com/list/----2018---1.html'
html_content = urllib.request.urlopen(URL).read().decode('GBK')
soup = BeautifulSoup(html_content, 'lxml')

# 获取页码，组合新的url列表
tag = soup.find('div', attrs={'class': 'v_page'}).get_text()
print(str(tag[-7] + tag[-6]))

print('****______我是分割线11111______***')


'''
sub_tags = soup.find_all('a', attars={'rel': 'nofollow'})
print(sub_tags)

print('****______我是分割线22222______***')
sub_tag = []
for tag in sub_tags:
    sub_tags.append(tag.get_text())
print(sub_tag)
'''





'''
url = 'https://www.qidian.com/all?action=1&orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1'
html_content = urllib.request.urlopen(url)
soup = BeautifulSoup(html_content, 'lxml')

tags = soup.find_all('li', attrs={'data-rid': re.compile('\d{1,2}')})
for tag in tags:
    items = []
    book_name = tag.find('h4').a.get_text()
    items.append(book_name)
    print(items)
'''