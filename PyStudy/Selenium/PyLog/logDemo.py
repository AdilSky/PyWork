#-*-coding:utf-8-*-
# Time:2017/9/27 10:44
# Author:YangYangJun


import logging
import sys
import os

import time,datetime

# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger()

# 指定logger输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

# 文件日志
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值

# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)

# 输出不同级别的log
logger.debug('this is debug info')
logger.info('this is information')
logger.warn('this is warning message')
logger.error('this is error message')
logger.fatal('this is fatal message, it is same as logger.critical')
logger.critical('this is critical message')

# 2016-10-08 21:59:19,493 INFO    : this is information
# 2016-10-08 21:59:19,493 WARNING : this is warning message
# 2016-10-08 21:59:19,493 ERROR   : this is error message
# 2016-10-08 21:59:19,493 CRITICAL: this is fatal message, it is same as logger.critical
# 2016-10-08 21:59:19,493 CRITICAL: this is critical message

# 移除一些日志处理器
logger.removeHandler(file_handler)


filepath = os.path.join(os.path.dirname(__file__),'logging.conf')

print filepath  # D:/WorkSpace/Python/Study/Selenium/PyLog\logging.conf

currentPath = os.path.join(os.getcwd(),'filename')
print currentPath  # D:\WorkSpace\Python\Study\Selenium\PyLog\filename

print __file__   # D:/WorkSpace/Python/Study/Selenium/PyLog/logDemo.py

print os.getcwd()  # D:\WorkSpace\Python\Study\Selenium\PyLog

print os.path.dirname(__file__)  # D:/WorkSpace/Python/Study/Selenium/PyLog



# 记录异常信息

try:
    1 / 0
except:
    # 等同于error级别，但是会额外记录当前抛出的异常堆栈信息
    logger.exception('this is an exception message')

# 2016-10-08 21:59:19,493 ERROR   : this is an exception message
# Traceback (most recent call last):
#   File "D:/Git/py_labs/demo/use_logging.py", line 45, in
#     1 / 0
# ZeroDivisionError: integer division or modulo by zero






















