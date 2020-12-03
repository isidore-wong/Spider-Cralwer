# --*-- coding:utf-8 --*--
import csv

'''
@File: csv_basic.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-12-3 18:35
'''

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])

with open('data1.csv', 'w') as csvfile1:
    fieldnames = ['id', 'name', 'age']
    writer1 = csv.DictWriter(csvfile1, fieldnames=fieldnames)
    writer1.writeheader()
    writer1.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer1.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer1.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})


