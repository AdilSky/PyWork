#-*-coding:utf-8-*-
# Time:2017/10/26 18:24
# Author:YangYangJun




import configparser

import os

rootPath = os.path.split(os.path.realpath(__file__))[0]

print rootPath

configPath = os.path.join(rootPath, 'config.ini')

print configPath


class ReadConfig:
    def __init__(self):
        # 实例化 cf
        self.cf = configparser.ConfigParser()
        # 处理配置文件中含中文字符的问题 ，UnicodeDecodeError: 'gbk' codec can't decode bytes in position 243-244: illegal multibyte sequence

        self.cf.read(configPath,encoding="utf-8-sig")


    def getMail(self,name):

        value =  self.cf.get('EMAIL',name)

        return value

    def getDB(self,name):

        value = self.cf.get('DB',name)

        return value
    def getHTTP(self,name):
        value = self.cf.get('HTTP',name)
        return value


# 测试方法

if __name__ == '__main__':

    rc = ReadConfig()
    print rc.getMail('Smtp_Server')