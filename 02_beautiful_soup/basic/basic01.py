# --*-- coding:utf-8 --*--
from bs4 import BeautifulSoup

'''
@File: basic01.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-11-25 11:39
'''

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())      # 将html结构化,以标准的缩进格式输出
print('**--------------**')
print(soup.title.text)
print(soup.p)
print(soup.p.name)      # 利用name属性获取节点的名称
print(soup.p.attrs)     # 利用attrs获取节点的属性
print(soup.p.attrs['name'])     #获取class/id等获取指定的属性
print(soup.p['class'])