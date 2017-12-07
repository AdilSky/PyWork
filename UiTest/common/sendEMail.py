#-*-coding:utf-8-*-
# Time:2017/10/26 20:03
# Author:YangYangJun

import smtplib
import unittest
import time
import UiTest.baseinfo as baseinfo
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import Wm_Api.readConfig as readConfig
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf8')

rC = readConfig.ReadConfig()



class EMail:

    def __init__(self):

        global server, sender, password, LReceiver, PReceiver
        global TReceiver, Text_Title, Msg_Title, Content_Type, Content_Disposition, Text_description

        # 通过配置文件获取基本信息
        print "--init--"
        server = rC.getMail('Smtp_Server')
        sender = rC.getMail('Smtp_Sender')
        password = rC.getMail('Password')
        LReceiver = rC.getMail('OnLine_Receiver')
        PReceiver = rC.getMail('Pre_Receiver')
        TReceiver = rC.getMail('Test_Receiver')
        Text_Title = rC.getMail('Text_Title')
        Msg_Title = rC.getMail('Msg_Title')
        Content_Type = rC.getMail('Content_Type')
        Content_Disposition = rC.getMail('Content_Disposition')
        Text_description = rC.getMail('Text_description')

        # print server
        #
        # print sender
        # print password
        # print LReceiver
        # print PReceiver
        # print TReceiver
        # print Text_Title
        # print Msg_Title
        # print Content_Type
        #
        # print Content_Disposition
        # print Text_description



        #实例化MIMEMultipart 对象，支持邮件及附件方式
        self.msg = MIMEMultipart()
        #采用related定义内嵌资源的邮件体
        #self.msg = MIMEMultipart('related')

        print "--init--"

    # Smtp_Server = 'smtp.mxhichina.com'
    # Smtp_Sender = 'dev@tenez.cn'
    # Password = 'Mall20151118'
    # OnLine_Receiver = ['yangyaojun@tenez.cn']
    # Pre_Receiver = ['yangyaojun@tenez.cn']
    # Test_Receiver = ['yangyaojun@tenez.cn']
    # Text_Title = '未名企鹅API自动化测试报告'
    # Msg_Title = '未名企鹅API自动化测试报告'
    # Content_Type = 'application/octet-stream'
    # Content_Disposition = 'attachment; filename="APITestReport.html"'
    # Text_description = 'API用例执行情况'

    def get_Result(self,reportFile):
        print "--get_Result--"
        driver = webdriver.Firefox()
        driver.maximize_window()
        ##得到测试报告路径
        result_url = "file://%s" % reportFile
        driver.get(result_url)
        time.sleep(5)
        result = driver.find_element_by_xpath("html/body/div[1]/p[4]").text
        self.result = result.split(':')
        driver.quit()
        print self.result[-1]
        self.setHeader(self.result[-1])
        #return result[-1]

        print "--get_Result--"

    def setHeader(self,result):
        #设置邮件主题
        print "--setHeader--"
        # 实例化MIMEMultipart 对象，支持邮件及附件方式
        # self.msg = MIMEMultipart()
        # 采用related定义内嵌资源的邮件体
        # self.msg = MIMEMultipart('related')
        now = time.strftime("%Y-%m-%d-%H_%M_%S")
        # 设置邮件主题
        self.msg['subject'] = Header('[执行结果：' + result + ']'+ Msg_Title + now, 'utf-8')
        print self.msg['subject']
        #self.msg['subject'] = Header( Msg_Title + now, 'utf-8')
        # 定义发件人，如果不写，发件人为空
        self.msg['From'] = sender
        # 定义收件人，如果不写，收件人为空
        self.msg['To'] = ",".join(TReceiver)
        print "--setHeader--"


    def setContent(self,reportFile):
        # 设置邮件正文
        print "--setContent--"
        f = open(reportFile, 'rb')
        # 读取测试报告正文
        self.mail_body = f.read()
        f.close()

        self.contentText = MIMEText(self.mail_body, 'html', 'UTF-8')
        self.contentText['Subject'] = Header(Text_Title, 'utf-8')

        self.msg.attach(self.contentText)
        self.setAccessory(self.mail_body)
        print "--setContent--"



    def setAccessory(self,mail_body):
        # 设置附件
        print "--setAccessory--"

        self.accessory = MIMEText(mail_body, 'html', 'utf-8')
        print Content_Type
        self.accessory['Content-Type'] = 'application/octet-stream'
        self.accessory["Content-Disposition"] = 'attachment; filename="APITestReport.html"'
        self.msg.attach(self.accessory)
        print "--setAccessory--"

    def sendEMail(self,reportFile):

        print "--sendEMail--"
        self.get_Result(reportFile)
        # self.setHeader("ok")
        self.setContent(reportFile)

        try:

            self.smtp = smtplib.SMTP(baseinfo.Smtp_Server, 25)
            sender = baseinfo.Smtp_Sender
            password = baseinfo.Smtp_Sender_Password
            receiver = baseinfo.Smtp_Receiver
            self.smtp.login(sender, password)

            # print server
            # #smtp = smtplib.SMTP()
            # self.smtp = smtplib.SMTP('smtp.mxhichina.com',25)
            # #smtp.connect()
            # print sender,password

            # self.smtp.login(sender, password)

            self.smtp.sendmail(sender, receiver, self.msg.as_string())
            self.smtp.quit()
            #self.logger.info("The test report has send to developer by email.")
        except smtplib.SMTPException as e:
            print(str(e))
        print "--sendEMail--"

# if __name__ == '__main__':
#
#     myEMail = EMail()
#     reportFilePath = os.path.join(readConfig.rootPath,'test_report')
#     reportFile = os.path.join(reportFilePath,'result-2017-10-25-12_06_13.html')
#     print reportFile
#     myEMail.sendEMail(reportFile)
#
#     pass






