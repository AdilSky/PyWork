#-*-coding:utf-8-*-
# Time:2017/10/23 22:56
# Author:YangYangJun
import os
import RequestsDemo.readConfig as readConfig
import logging
from datetime import datetime
import threading

localReadConfig = readConfig.ReadConfig()




class Log:

    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")
        print resultPath


if __name__ == "__main__":
   log = Log()
