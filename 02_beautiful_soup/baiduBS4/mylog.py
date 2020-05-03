# _*_ coding:utf-8 _*_

import logging
import getpass
import sys

"""
@author: Isidore
@email:616132717@qq.com
@file: mylog.py.py
@time: 2018/12/16  20:19
@version: 1.0
"""

"""
程序目的：logging模块输出
getpass模块见readme
sys.argv模块见readme
"""

# 定义MyLog类


class MyLog(object):
    # 类MyLog的构造函数
    def __init__(self):
        self.user = getpass.getuser()
        self.logger = logging.getLogger(self.user)
        self.logger.setLevel(logging.DEBUG)

# 日志文件名
        self.logFile = sys.argv[0][0:-3] + '.log'

        # 自定义日志的输出格式，这个格式可以被文件输出流和屏幕输出流调用；
        self.formatter = logging.Formatter(
            '%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s\r\n')

# 日志显示到屏幕上并输出到日志文件内
        # 创建一个文件输出流；
        self.logHand = logging.FileHandler(self.logFile, encoding='utf8')
        # 添加格式花输出，即调用我们上面所定义的格式，换句话说就是给这个handler选择一个格式；
        self.logHand.setFormatter(self.formatter)
        self.logHand.setLevel(logging.DEBUG)

        # 创建一个屏幕输出流；
        self.logHandSt = logging.StreamHandler()
        # 添加格式花输出，即调用我们上面所定义的格式，换句话说就是给这个handler选择一个格式；
        self.logHandSt.setFormatter(self.formatter)
        self.logHandSt.setLevel(logging.DEBUG)

        # logger对象可以创建多个文件输出流和屏幕输出流
        self.logger.addHandler(self.logHand)
        self.logger.addHandler(self.logHandSt)

# 日志的5个级别对应以下的5个函数
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    mylog = MyLog()
    mylog.debug(u"I'm debug 测试中文")
    mylog.info("I'm info")
    mylog.warn("I'm warn")
    mylog.error(u"I'm error 测试中文")
    mylog.critical("I'm critical")
