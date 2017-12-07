#-*-coding:utf-8-*-
# Time:2017/10/25 21:16
# Author:YangYangJun

import logging

from datetime import datetime

import threading

import ApiTest.readConfig as readConfig
import os



class Log:
    def __init__(self):
        global logPath, rootPath, dateFile

        rootPath = readConfig.rootPath

        print rootPath

        logPath = os.path.join(rootPath, "Log")
        print logPath

        dateFile = os.path.join(logPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        print dateFile
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        if not os.path.exists(dateFile):
            os.mkdir(dateFile)
        # defined logger  获取 logger 实例
        self.logger = logging.getLogger()

        # defined log level 设置级别
        # 2016-10-08 21:59:19,493 INFO    : this is information
        # 2016-10-08 21:59:19,493 WARNING : this is warning message
        # 2016-10-08 21:59:19,493 ERROR   : this is error message
        # 2016-10-08 21:59:19,493 CRITICAL: this is fatal message, it is same as logger.critical
        # 2016-10-08 21:59:19,493 CRITICAL: this is critical message

        self.logger.setLevel(logging.INFO)

        # defined handler  设置日志输入文件
        handler = logging.FileHandler(os.path.join(dateFile, "ApiTestLog.log"))
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
    def get_log():

        if MyLog.log is None:
            # 获取线程
            MyLog.mutex.acquire()
            # 实例化Log
            MyLog.log = Log()
            # 释放线程
            MyLog.mutex.release()

        return MyLog.log


# if __name__ == '__main__':
#     getlog = MyLog()
#     getlog.get_log()

