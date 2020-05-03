# _*_ coding:utf-8 _*_

import pymysql

"""
@author: Isidore
@email:616132717@qq.com
@file: save2mysql.py
@time: 2018/12/16  21:43
@version: 1.0
"""

"""
程序目的：将数据保存到mysql数据库中
"""


class SavebooksData(object):
    def __init__(self,items):
        self.host = 'localhost'
        self.port = '3306'
        self.user = 'root'
        self.password = 'root111111'
        self.db = 'bs4DB'

        self.run(items)

    def run(self, items):
        conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db
        )

        cur = conn.cursor()
        for item in items:
            cur.execute(
                "INSERT INTO qidian_books(category_name, book_name, words_num, author_name)  values(%s, %s, %s, %s)",
                (item.categoryName, item.bookName, item.wordsNum, item.authorName))
        cur.close()
        conn.commit()
        conn.close()


if __name__ == '__main__':
    pass
