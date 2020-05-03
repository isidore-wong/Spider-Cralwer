#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import pymysql

"""
@version: 1.0
@author: isidore wong
@contact: isidore_wong@163.com
@site: https://github.com/isidore-wong
@file: review_sql.py
@time: 2019/9/6 9:49
"""

"""
program purpose: save data to mysql
"""

# 向数据库URL数据表中插入口碑内容URL
class SaveReviewUrlData(object):
    def __init__(self, items):
        self.host = 'localhost'
        self.port = '3306'
        self.user = 'root'
        self.password = 'root123456'
        self.db = 'car_review_db'

        self.insertUrlData(items)

    # 连接数据库
    def _getconn(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db
            )
        except pymysql.Error as e:
            print("数据库连接失败!")

    # 关闭数据库连接
    def _closeconn(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print("数据库关闭失败!")

    # 向数据库中插入数据
    def insertUrlData(self, items):
        try:
            self._getconn()
            cur = self.conn.cursor()
            for item in items:
                cur.execute("INSERT INTO review_url_tb(content_url) VALUES(%s)",
                            (item.content_url))
            cur.commit()        # commit the operation to database
            print("数据存储成功!")
        except pymysql.DataError as e:
            print(e)
            self.conn.rollback()        # database rollback
        finally:
            if cur:
                cur.close()
            self._closeconn()


# 向数据库content数据表中插入口碑评论数据
class SaveReviewContentData(object):
    def __init__(self, items):
        self.host = 'localhost'
        self.port = '3306'
        self.user = 'root'
        self.password = 'root123456'
        self.db = 'car_review_db'

        self.insertContentData(items)

    # 连接数据库
    def _getconn(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db
            )
        except pymysql.Error as e:
            print("数据库连接失败!")

    # 关闭数据库连接
    def _closeconn(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print("数据库关闭失败!")

    # 向数据库中插入数据
    def insertContentData(self, items):
        try:
            self._getconn()
            cur = self.conn.cursor()
            for item in items:
                cur.execute(
                    "INSERT INTO review_tb(content_title, pub_date, review_level, visit_count, user_id,brand_name, spec_name, city_name, bought_dlr, bought_date, bought_price, purpose, space_score, power_socre, maneuverability_score, oil_socre, comfortableness_score, apperance_socre, internal_score, costefficient_score, Satisfaction, car_merit, car_defect, space_feeling, power_feeling, maneuverability_feeling, oil_feeling, comfortableness_feeling, apperance_feeling, internal_feeling, costefficient_feeling, bought_reason) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, )",
                    (items.content_title, items.pub_date, items.review_level, items.visit_count, items.user_id, items.brand_name, items.spec_name, items.city_name, items.bought_dlr, items.bought_date, items.bought_price, items.purpose, items.space_score, items.power_socre, items.maneuverability_score, items.oil_socre, items.comfortableness_score, items.apperance_socre, items.internal_score, items.costefficient_score,items.Satisfaction, items.car_merit, items.car_defect, items.space_feeling, items.power_feeling, items.maneuverability_feeling, items.oil_feeling, items.comfortableness_feeling, items.apperance_feeling, items.internal_feeling, items.costefficient_feeling, items.bought_reason)
                )
            cur.commit()  # commit the operation to database
            print("数据存储成功!")
        except pymysql.DataError as e:
            print(e)
            self.conn.rollback()  # database rollback
        finally:
            if cur:
                cur.close()
            self._closeconn()







