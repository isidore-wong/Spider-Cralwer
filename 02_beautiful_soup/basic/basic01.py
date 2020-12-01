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

# 关联选择  有时候不能做到一步就选到想要的节点元素，需要先选中某一个节点元素，然后以它为基准再选择它的子节点、父节点、兄弟节点等
html1 = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story"
"""
soup1 = BeautifulSoup(html1, 'lxml')
print('**------p-------**')
print(soup1.p.contents)
print(soup1.p.children)     # 返回p的子孙节点，返回的结果是生成器类型，采用枚举输出相应的内容
for i, child in enumerate(soup1.p.children):
    print(i, child)


# 返回所有的子孙节点，可以调用descendants属性
# descendants会递归查询所有子节点，得到所有的子孙节点。
print('**-------descendants------------**')
print(soup1.p.descendants)
for i, child in enumerate(soup1.p.descendants):
    print(i, child)

# 如果要获取某个节点元素的父节点，可以调用parent属性
html2 = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
        <p class="story">...</p>
"""
soup2 = BeautifulSoup(html2, 'lxml')
print('**---------父节点----------**')
print(soup2.a.parent)     # 直接父节点
print('**---------所有祖先节点----------**')
print(list(enumerate(soup2.a.parents)))      # 所有的祖先节点

# 兄弟节点
html3 = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""
soup3 = BeautifulSoup(html3, 'lxml')
print('**-----兄弟节点-----**')
print('Next Sibling', soup3.a.next_sibling)     # 下一个兄弟节点
print('Previous Sibling', soup3.a.previous_sibling)     # 上一个兄弟节点
print('next siblings', list(enumerate(soup3.a.next_siblings)))      # 前面所有的兄弟节点
print('previous siblings', list(enumerate(soup3.a.previous_siblings)))      # 后面的所有兄弟节点
