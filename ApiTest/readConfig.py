#-*-coding:utf-8-*-
# Time:2017/10/24 23:37
# Author:YangYangJun

from configparser import ConfigParser
import os


#  这里这样写是获取当前文件的绝对目录不会受到调用改程序的其他文件影响。
rootPath = os.path.split(os.path.realpath(__file__))[0]
# 下面这种写法是，会根据执行程序所在的目录而获取执行程序的目录，而不是当前文件所在的目录。所以使用上面的写法
# os.getcwd()



configPath = os.path.join(rootPath,'config.ini')



class ReadConfig:

    def __init__(self):

        # 实例化 ConfigParser
        self.cf = ConfigParser()
        self.cf.read(configPath)

    # 获取邮件相关信息
    def get_MailInfo(self,name):
        value = self.cf.get('EMAIL',name)
        return value
    # 获取数据库相关信息
    def get_DB(self,name):
        value = self.cf.get('DB',name)
        return value

    # 获取http相关信息
    def get_Http(self, name):
        value = self.cf.get('HTTP', name)
        return value


# if __name__ == '__main__':
#
#     readCf = ReadConfig()
#
#     print readCf.get_MailInfo("Password")
#
#     pass

