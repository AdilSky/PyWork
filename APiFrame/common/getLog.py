#-*-coding:utf-8-*-
# Time:2017/10/23 22:56
# Author:YangYangJun
import os
import APiFrame.readConfig as readConfig
import logging
from datetime import datetime
import threading




class Log:

    def __init__(self):
        global logPath, testReport, proDir
        proDir = readConfig.proDir
        testLog = os.path.join(proDir, "testLog")
        # create result file if it doesn't exist
        if not os.path.exists(testLog):
            os.mkdir(testLog)
        # defined test result file name by localtime
        logPath = os.path.join(testLog, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        print  logPath
        # create test result file if it doesn't exist
        if not os.path.exists(logPath):
            os.mkdir(logPath)
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
        handler = logging.FileHandler(os.path.join(logPath, "ApiTestLog.log"))
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

