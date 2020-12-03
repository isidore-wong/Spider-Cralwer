# --*-- coding:utf-8 --*--
import json

'''
@File: basic_json.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-12-2 8:44
'''

'''
json：通过对象和数组的组合来表示数据，构造简洁但是结构化程度非常高，是一种轻量级的数据交换格式
字符串、数字、对象、数组等任何对象类型都可以通过json来表示，数据结构为 {key1：value1, key2：value2, ...} 的键值对结构
可以调用JSON库的loads()方法将字符串传化为字典，dumps()将字典转化为字符串
'''

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''