#-*-coding:utf-8-*-
# Time:2017/10/17 15:45
# Author:YangYangJun



import os
import codecs
import configparser



# 过去当前文件的绝对完整path
print os.path.realpath(__file__)   # D:\WorkSpace\Python\PyStudy\Python\PyApi\PyRequests\RequestStudy\readConfig.py
# 截取文件名获取绝对路径
print os.path.split(os.path.realpath(__file__))  #('D:\\WorkSpace\\Python\\PyStudy\\Python\\PyApi\\PyRequests\\RequestStudy', 'readConfig.py')
# 获取绝对路径的第一个元素
proDir = os.path.split(os.path.realpath(__file__))[0]  # D:\WorkSpace\Python\PyStudy\Python\PyApi\PyRequests\RequestStudy

print proDir

print  "*****-------****"
configPath = os.path.join(proDir, "config.ini")
print configPath

print  "*****-------****"
class ReadConfig():
    def __init__(self):
        fd = open(configPath)
        data = fd.read()
        print "*************"
        print "data", data
        print "*************"

        print "------------"
        print data[:3]
        print "+++++++++++++"
        print data[3:]
        print "------------"

        print codecs.BOM_UTF8

        print "^^^^^^^^^^^^^^"
        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

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


if __name__ == "__main__":
    getdata = ReadConfig()
    print  getdata.get_db("host")
    print  getdata.get_http("port")
    print  getdata.get_email("Smtp_Receiver")



