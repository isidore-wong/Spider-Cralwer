# --*-- coding:utf-8 --*--
import re

'''
@File: basic04.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-11-23 11:26
'''

'''
match/search/findall/sub都是用来处理字符串的方法
compile可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用
compile还可以传入修饰符，例如re.S等修饰符，这样在search、findall等方法中就不需要额外传了
所以，compile方法可以说是给正则表达式做了一层封装，以便我们更好地复用
'''
content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)