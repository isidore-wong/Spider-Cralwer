# --*-- coding:utf-8 --*--
import re

'''
@File: basic03.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-11-23 10:34
'''

'''
match()是从字符串的开头开始匹配的，一旦开头不匹配，整个匹配就会失败
search():在匹配过程中会扫描整个字符串，然后返回第一个成功匹配的结果
'''

# 待匹配的HTML文本
html = '''<div id="songs-list">
<h2 class="title"> 经典老歌 </h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2"> 一路上有你 </li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐"> 沧海一声笑 </a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦"> 往事随风 </a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond"> 光辉岁月 </a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳"> 记事本 </a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君"> 但愿人长久 </a>
</li>
</ul>
</div>'''


# 提取class为active的li节点内部的超链接包含的歌手名和歌名
# rule = '<li.*?active.*?singer="(.*?)">(.*?)</a>'
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print("singer:{}  sing:{}".format(result.group(1), result.group(2)))

print("***---------------------***")

# 不加class为active，提取信息将返回第一个匹配成功的结果
result1 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print("singer:{}  sing:{}".format(result1.group(1), result1.group(2)))

print("***---------------------***")


'''
search是返回第一个匹配成功的结果，如果想要返回所以匹配结果，使用findall
'''
results = re.findall('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
print((results))
print(type(results))
for resu in results:
    print("singer:{}  sing:{}".format(resu[0], resu[1]))
print("***---------------------***")

# 除了使用正则表达式提取信息外，有时候还需要借助它来修改文本
# 把文本中的数字去掉
content = '54aK54yr5oiR54ix5L2g'
result2 = re.sub('\d+', '', content)
print(result2)

