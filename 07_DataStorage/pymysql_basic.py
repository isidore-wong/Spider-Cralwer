# --*-- coding:utf-8 --*--
import pymysql

'''
@File: pymysql_basic.py
@Author: Hayes Wong
@Email: 616132717@qq.com
@Time:  2020-12-3 18:44
'''

# 首先尝试连接一下数据库。假设当前的 MySQL 运行在本地，用户名为 root，密码为 123456，运行端口为 3306。这里利用 PyMySQL 先连接 MySQL，
# 然后创建一个新的数据库，名字叫作 spiders
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
# 调用 fetchone 方法获得第一条数据
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()


# 新创建一个数据表 students
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, ' \
      'PRIMARY KEY (id))'
cursor.execute(sql)
db.close()


# 插入数据
id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(% s, % s, % s)'
try:
    cursor.execute(sql, (id, user, age))
    # 需要执行 db 对象的 commit 方法才可实现数据插入
    db.commit()
except:
    db.rollback()
db.close()


# 根据字典动态构造，元组也动态构造，实现通用的插入方法
data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 20
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['% s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
   if cursor.execute(sql, tuple(data.values())):
       print('Successful')
       db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
db.close()

# 更新数据，实现一种去重的方法，如果数据存在，则更新数据；如果数据不存在，则插入数据
data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 21
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['% s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'\
    .format(table=table, keys=keys, values=values)
update = ','.join(["{key} = % s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()




