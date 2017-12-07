#-*-coding:utf-8-*-
# Time:2017/10/25 21:16
# Author:YangYangJun

import logging

from datetime import datetime

import threading

import Wm_UIDemo.readConfig as RC
import os



class Log:
    '定义Log类'
    def __init__(self,name):
        '重构__init__方法，传入logger的参数，name，这样打印的日志就是传入参数的的名字'
        global logPath, rootPath, dateFile

        rootPath = RC.rootPath

        print rootPath

        logPath = os.path.join(rootPath, "Log")
        print logPath

        dateFile = os.path.join(logPath, str(datetime.now().strftime("%Y%m%d")))
        print dateFile
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        if not os.path.exists(dateFile):
            os.mkdir(dateFile)
        # defined logger  获取 logger 实例
        self.logger = logging.getLogger(name)

        # defined log level 设置级别，如下级别依次递增，设置高级别的，会过滤不显示低级别的日志。
        # 2016-10-08 21:59:19,493 INFO    : this is information
        # 2016-10-08 21:59:19,493 WARNING : this is warning message
        # 2016-10-08 21:59:19,493 ERROR   : this is error message
        # 2016-10-08 21:59:19,493 CRITICAL: this is fatal message, it is same as logger.critical
        # 2016-10-08 21:59:19,493 CRITICAL: this is critical message

        self.logger.setLevel(logging.INFO)

        # defined handler  设置日志输入文件
        # 日志名
        logFileName = 'ApiTestLog' + str(datetime.now().strftime('%H%M%S')) +'.log'
        handler = logging.FileHandler(os.path.join(dateFile, logFileName))
        # defined formatter  指定logger输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter  可以通过setFormatter指定输出格式
        handler.setFormatter(formatter)
        # add handler 为logger添加的日志处理器
        self.logger.addHandler(handler)


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log(name):

        if MyLog.log is None:
            # 获取线程
            MyLog.mutex.acquire()
            # 实例化Log
            MyLog.log = Log(name)
            # 释放线程
            MyLog.mutex.release()

        return MyLog.log


if __name__ == '__main__':
    getlog = MyLog()
    getlog.get_log()

