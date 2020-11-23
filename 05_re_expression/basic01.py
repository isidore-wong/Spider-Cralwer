# --*-- coding:utf-8 --*--
import re

'''
@File: basic01.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-11-23 9:11
'''

'''
Description:
'''

# 正则表达式基础：基本匹配规则+match()的使用
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))

# re，使用^Hello\s\d{3}\s\d{4}\s\w{10}匹配字符串内容
result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print('**-----------------------**')

'''
上例使用match()可以得到字符串内容，如果需要提取字符串的一部分内容，使用()括号将想提取的子字符串括起来
()标记了一个子表达式的开始和结束位置，被标记的每个子表达式会依次对应每一个分组，调用group方法传入分组的索引即可获取提取的结果。
'''
content = 'Hello 1234567 World_This is a Regex Demo'
result1 = re.match('^Hello\s(\d+)\s(\w+)', content)
print(result1)
print(result1.group(0))     # 所匹配的整个字符串
print(result1.group(1))     # 第一个被()包围的匹配结果
print(result1.group(2))     # 第二个被()包围的匹配结果

