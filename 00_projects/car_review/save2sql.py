#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import pymysql

"""
@version: 1.0
@author: isidore wong
@contact: isidore_wong@163.com
@site: https://github.com/isidore-wong
@file: save2sql.py
@time: 2019/9/6 9:49
"""

"""
program purpose: save data to mysql
"""


class SaveReviewData(object):
    def __init__(self, items):
        self.host = 'localhost'
        self.post = '3306'
        self.user = 'root'
        self.password = '46120201'
        self.db = 'car_review_db'

        self.insertData(items)

    # get database connection
    def _getconn(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                post=self.port,
                user=self.user,
                password=self.password,
                db=self.db
            )
        except pymysql.Error as e:
            print("数据库连接失败!")

    # close database connection
    def _closeconn(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print("数据库关闭失败!")

    # insert data into database
    def insertData(self, items):
        try:
            self._getconn()
            cur = self.conn.cursor()
            for item in items:
                cur.execute("INSERT INTO review_url(post_id, post_name, pub_time, post_url) VALUES(%s, %s, %s, %s)",
                            (item.postID, item.postName, item.pubTime, item.postUrl))
            cur.commit()        # commit the operation to database
            print("数据存储成功!")
        except pymysql.DataError as e:
            print(e)
            self.conn.rollback()        # database rollback
        finally:
            if cur:
                cur.close()
            self._closeconn()

    if __name__ == "__main__":
        pass







