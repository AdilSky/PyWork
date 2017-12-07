#-*-coding:utf-8-*-
# Time:2017/10/17 15:45
# Author:YangYangJun



import os

import configparser



# 获取绝对路径的第一个元素
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")

class ReadConfig():
    def __init__(self):
        fd = open(configPath)
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value





