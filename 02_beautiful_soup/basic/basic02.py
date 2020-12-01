# --*-- coding:utf-8 --*--
from bs4 import BeautifulSoup

'''
@File: basic02.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-12-1 10:42
'''

'''
调用BeautifoulSoup的方法选择器，传入相应参数，灵活查询与提取信息，比如find_all和find等
basic01主要是通过属性来选择的，这种方法非常快，但是如果进行比较复杂的选择的话，它就比较烦琐，不够灵活了
find_all(name , attrs , recursive , text , **kwargs)
find_parents 和 find_parent：前者返回所有祖先节点，后者返回直接父节点。
find_next_siblings 和 find_next_sibling：前者返回后面所有的兄弟节点，后者返回后面第一个兄弟节点。
find_previous_siblings 和 find_previous_sibling：前者返回前面所有的兄弟节点，后者返回前面第一个兄弟节点。
find_all_next 和 find_next：前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点。
find_all_previous 和 find_previous：前者返回节点前所有符合条件的节点，后者返回第一个符合条件的节点。
'''
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

# name
soup = BeautifulSoup(html, 'lxml')
print(soup.find(name='ul'))     # find返回第一个匹配到的ul
print(soup.find_all(name='ul'))     # find_all返回所有匹配到的ul

# 嵌套查询，查询其子节点
print('****嵌套查询子节点***')
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.text)



# attrs:通过传入一些属性来进行查询
html1 ='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup1 = BeautifulSoup(html1, 'lxml')
print('****通过attrs属性提取信息*****')
print(soup1.find_all(attrs={'id': 'list-1'}))
print(soup1.find_all(attrs={'class': 'list'}))
print('-------------------')
print(soup1.find_all(attrs={'name': 'elements'}))

