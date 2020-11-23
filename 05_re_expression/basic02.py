# --*-- coding:utf-8 --*--
import re

'''
@File: basic02.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-11-23 9:31
'''

# 使用\s + \d的方式过于复杂与麻烦，可以采用万能的匹配方式(. * + ?)等方式
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*Demo$', content)
print(result)
print(result.group())
print('**_______________________**')

# .*属于贪婪匹配，会匹配尽可能多的字符，因此有些时候并不是我们希望得到的结果，这个时候就需要非贪婪匹配了
# 我们想获取’1234567‘7个数字，使用贪婪匹配的结果是
result1 = re.match('^He.*(\d+).*Demo$', content)
print(result1)
print(result1.group())
print(result1.group(1))     # 由于使用贪婪匹配，导致(\d+)仅匹配到7这一个数字，与我们所希望的不符

# 使用非贪婪匹配.*?   加上?后会尽可能少的去匹配
result2 = re.match('^He.*?(\d+).*Demo$', content)
print('**_______________________**')
print(result2)
print(result2.group())
print(result2.group(1))     # 使用非贪婪匹配.*?  得到我们所希望的结果
print('**_______________________**')

# 如果.*?匹配的结果在结尾，可能匹配不到任何内容，因为它是尽可能少的匹配字符
content1 = 'http://weibo.com/comment/kEraCN'
result3 = re.match('http.*?/comment/(.*?)', content1)
result4 = re.match('http.*?/comment/(.*)', content1)
print('result3', result3.group(1))      # 因为使用非贪婪匹配，匹配不到字符
print('result4', result4.group(1))
print('**_______________________**')


# 当非贪婪匹配遇到换行符的时候，需要采用一些修饰符加以修正，使得匹配成功
content2 = '''Hello 1234567 World_This
is a Regex Demo'''
result5 = re.match('^He.*?(\d+).*?Demo$', content2)
# print(result5.group(1))     # 匹配的是除换行符之外的任意字符，当遇到换行符时，.*? 就不能匹配了，所以导致匹配失败。这里只需加一个修饰符 re.S
result6 = re.match('^He.*?(\d+).*?Demo$', content2, re.S)
print('result6', result6.group(1))

# 转义匹配，当目标字符串里面就包含任意字符时，在前面加反斜线转义一下即可
content3 = '(百度) www.baidu.com'
result7 = re.match('\(百度\) www\.baidu\.com', content3)
print(result7.group())

