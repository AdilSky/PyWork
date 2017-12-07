#-*-coding:utf-8-*-
# Time:2017/10/26 20:03
# Author:YangYangJun

import smtplib
import sys
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from selenium import webdriver

import Wm_UIDemo.baseinfo as baseinfo
import Wm_UIDemo.test_report.readConfig as readConfig

reload(sys)
sys.setdefaultencoding('utf8')

rC = readConfig.ReadConfig()



class EMail:

    def __init__(self):

        global server, sender, password,Content_Type, Content_Disposition, Text_description


        # 通过配置文件获取基本信息
        print "--init--"
        server = rC.getMail('Smtp_Server')
        self.sender = rC.getMail('Smtp_Sender')
        self.password = rC.getMail('Password')
        self.LReceiver = rC.getMail('OnLine_Receiver')
        self.PReceiver = rC.getMail('Pre_Receiver')
        self.TReceiver = rC.getMail('Test_Receiver')
        # self.Text_Title = rC.getMail('Text_Title')
        # self.Msg_Title = rC.getMail('Msg_Title')
        # Content_Type = rC.getMail('Content_Type')
        # Content_Disposition = rC.getMail('Content_Disposition')
        # Text_description = rC.getMail('Text_description')



        #实例化MIMEMultipart 对象，支持邮件及附件方式
        self.msg = MIMEMultipart()
        #采用related定义内嵌资源的邮件体
        #self.msg = MIMEMultipart('related')

        print "--init--"

    #
    # def get_Result(self,reportFile):
    #     print "--get_Result--"
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     ##得到测试报告路径
    #     result_url = "file://%s" % reportFile
    #     driver.get(result_url)
    #     time.sleep(5)
    #     result = driver.find_element_by_xpath("html/body/div[1]/p[4]").text
    #     self.result = result.split(':')
    #     driver.quit()
    #     print self.result[-1]
    #     # self.setHeader(self.result[-1])
    #     return self.result[-1]
    #
    #     print "--get_Result--"
    #
    # def send_Mail(self,file_new):
    #     f = open(file_new, 'rb')
    #     # 读取测试报告正文
    #     mail_body = f.read()
    #     f.close()
    #
    #     result = self.get_Result(file_new)
    #
    #     try:
    #         print server
    #         print "上面是server 的信息"
    #         print baseinfo.Smtp_Server
    #         print "上面是 baseinfo.Smtp_Server 的信息"
    #         smtp = smtplib.SMTP(server, 25)
    #         #smtp = smtplib.SMTP('smtp.mxhichina.com', 25)
    #         #smtp = smtplib.SMTP(baseinfo.Smtp_Server, 25)
    #         #sender = baseinfo.Smtp_Sender
    #
    #         sender = self.sender
    #         print sender
    #
    #         #password = baseinfo.Smtp_Sender_Password
    #
    #         password = self.password
    #         print password
    #         #receiver = baseinfo.Smtp_Receiver_test
    #         receiver = []
    #         receiver.append(self.TReceiver)
    #         #receiver = self.TReceiver
    #         print receiver
    #         print baseinfo.Smtp_Receiver_test
    #         smtp.login(sender, password)
    #         msg = MIMEMultipart()
    #         # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
    #         # 发送正文
    #         text = MIMEText(mail_body, 'html', 'utf-8')
    #         text['Subject'] = Header('未名企鹅UI自动化测试报告', 'utf-8')
    #         msg.attach(text)
    #         # 发送附件
    #         now = time.strftime("%Y-%m-%d-%H_%M_%S")
    #         # Header()用于定义邮件标题
    #         msg['Subject'] = Header('[执行结果：'+ result +']' + '未名企鹅UI自动化测试报告' + now, 'utf-8')
    #         msg_file = MIMEText(mail_body, 'html', 'utf-8')
    #         msg_file['Content-Type'] = 'application/octet-stream'
    #         msg_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    #         msg.attach(msg_file)
    #         # 定义发件人，如果不写，发件人为空
    #         msg['From'] = sender
    #         # 定义收件人，如果不写，收件人为空
    #         msg['To'] = ",".join(receiver)
    #         tmp = smtp.sendmail(sender, receiver, msg.as_string())
    #         print tmp
    #         smtp.quit()
    #         return True
    #     except smtplib.SMTPException as e:
    #         print(str(e))
    #         return False


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
        self.msg['subject'] = Header('[执行结果：' + result + ']'+ '未名企鹅API自动化测试报告' + now, 'utf-8')
        print self.msg['subject']
        #self.msg['subject'] = Header( Msg_Title + now, 'utf-8')

        print "--setHeader--"


    def setContent(self,reportFile):
        # 设置邮件正文
        print "--setContent--"
        f = open(reportFile, 'rb')
        # 读取测试报告正文
        self.mail_body = f.read()
        f.close()

        self.contentText = MIMEText(self.mail_body, 'html', 'UTF-8')
        self.contentText['Subject'] = Header('未名企鹅API自动化测试报告', 'utf-8')

        self.msg.attach(self.contentText)
        self.setAccessory(self.mail_body)
        print "--setContent--"



    def setAccessory(self,mail_body):
        # 设置附件
        print "--setAccessory--"

        self.accessory = MIMEText(mail_body, 'html', 'utf-8')
        #print Content_Type
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
            print server
            #self.smtp = smtplib.SMTP(server,25)
            self.smtp = smtplib.SMTP('smtp.mxhichina.com',25)
            #smtp.connect()
            print self.sender,self.password
            self.smtp.login(self.sender,self.password)
            print self.TReceiver
            receiver = baseinfo.Smtp_Receiver_test
            print receiver
            receiver = []
            receiver.append(self.TReceiver)
            print receiver
            # 定义发件人，如果不写，发件人为空
            self.msg['From'] = self.sender
            # 定义收件人，如果不写，收件人为空
            self.msg['To'] = ",".join(receiver)
            self.smtp.sendmail(self.sender, self.TReceiver, self.msg.as_string())
            self.smtp.quit()
            return True
            #self.logger.info("The test report has send to developer by email.")
        except smtplib.SMTPException as e:
            print(str(e))
        print "--sendEMail--"



#
# if __name__ == '__main__':
#
#     myEMail = EMail()
#     reportFilePath = os.path.join(readConfig.rootPath,'test_report')
#     reportFile = os.path.join(reportFilePath,'result-2017-10-25-12_06_13.html')
#     print reportFile
#     myEMail.sendEMail(reportFile)
#
#     pass






