# --*-- coding:utf-8 --*--
from bs4 import BeautifulSoup

'''
@File: basic03.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-12-1 11:18
'''
'''
Beautiful Soup还提供了另外一种选择器，那就是CSS选择器,
使用CSS选择器，只需要调用select方法，传入相应的CSS选择器即可
'''
html = '''
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

soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel'))
print('------------------------')
print(soup.select('.panel .panel-heading'))
print('------------------------')
print(soup.select('ul li'))
print('------------------------')
print(soup.select('#list-2 .element'))
print('------------------------')
for li in soup.select('li'):
    print(li.get_text())