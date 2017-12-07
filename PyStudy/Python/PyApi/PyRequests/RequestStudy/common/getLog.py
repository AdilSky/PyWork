#-*-coding:utf-8-*-
# Time:2017/10/23 22:56
# Author:YangYangJun

import logging

from datetime import datetime
import readConfig as readConfig

import threading

class Log:

    def __init__(self):
        global logPath, resultPath, proDir

        proDir = readConfig.proDir

        print proDir

        pass


if __name__ == "__main__":
    log = Log()