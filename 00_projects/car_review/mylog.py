#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import logging
import getpass
import sys

"""
@version: 1.0
@author: isidore wong
@contact: isidore_wong@163.com
@site: https://github.com/isidore-wong
@file: mylog.py
@time: 2019/8/9 14:10
"""

"""
program purpose:
record the status and results of program running
"""

# define the class of MyLog
class MyLog(object):

    # the constructor of MyLog
    def __init__(self):
        self.user = getpass.getuser()
        self.logger = logging.getLogger(self.user)
        self.logger.setLevel(logging.DEBUG)

        # define logging name and file format
        self.logFile = sys.argv[0][0:-3] + '.log'
        self.formatter = logging.Formatter(
            '%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s\r\n')

        # file handler
        self.logHand = logging.FileHandler(self.logFile, encoding='utf-8')
        self.logHand.setFormatter(self.formatter)
        self.logHand.setLevel(logging.DEBUG)

        # stream handler
        self.logHandSt = logging.StreamHandler()
        self.logHandSt.setFormatter(self.formatter)
        self.logHandSt.setLevel(logging.DEBUG)

        self.logger.addHandler(self.logHand)
        self.logger.addHandler(self.logHandSt)


    # the five level of logging module
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    mylog = MyLog()
    mylog.debug("I am debug 测试中文")
    mylog.info("I am info")
    mylog.warn("I am warn")
    mylog.error("I am error 测试中文")
    mylog.critical("I am critical")



