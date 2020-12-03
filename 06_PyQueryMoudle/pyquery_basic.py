# --*-- coding:utf-8 --*--
from pyquery import PyQuery as pq
import requests

'''
@File: pyquery_basic.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-12-1 14:06
'''

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
# CSS选择器
print(doc('#container .list li'))
print('----------list-----------')
items = doc('.list')
print(items)
# find方法
print('----------li-----------')
lis = items.find('li')
print(lis)

print('---------pq------------')
doc1 = pq(requests.get(url='http://cuiqingcai.com').text)
doc2 = pq(url='http://cuiqingcai.com')
print(doc1('title'))
print(doc2('title'))

print('---------子节点------------')
print(items.children('.active'))
print('---------父节点------------')
print(items.parent())
print('---------兄弟节点------------')
print(doc('.list .item-0.active').siblings())
print('---------生成器 遍历------------')
lis = doc('li').items()
for li in lis:
    print(li, type(li))


# 调用 attr() 方法来获取属性
print('---------调用attr()方法来获取属性------------')
print(doc('.item-0.active a').attr('href'))
print('---------获取所有的a------------')
a = doc('a')
for item in a.items():
    print(item.attr('href'))

# 可以调用text()方法来实现获取文本信息
print('---------调用text()方法来获取文本信息------------')
print(a.text())

# pyquery的节点操作， 提供了一系列方法来对节点进行动态修改，比如为某个节点添加一个class  addClass ，移除某个节点 removeClass
print('---------节点操作------------')
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

# 用attr、 text和html方法来改变节点内部的内容
print('---------节点操作1------------')
html1 = '''
<ul class="list">
     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
doc3 = pq(html1)
li = doc3('.item-0.active')
print(li)
li.attr('name', 'link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)

# 伪类选择器
print('---------伪类选择器------------')
html2 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc4 = pq(html2)
# 第一个 li 节点、
li = doc4('li:first-child')
print(li)
# 最后一个 li 节点、
li = doc4('li:last-child')
print(li)
# 第二个 li 节点、
li = doc4('li:nth-child(2)')
print(li)
# 第三个 li 之后的 li 节点、
li = doc4('li:gt(2)')
print(li)
# 偶数位置的 li 节点、
li = doc4('li:nth-child(2n)')
print(li)
# 包含 second 文本的 li 节点
li = doc4('li:contains(second)')
print(li)