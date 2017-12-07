#-*-coding:utf-8-*-
# Time:2017/10/28 8:50
# Author:YangYangJun


import sys
reload(sys)
sys.setdefaultencoding('utf8')

import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner
from common.EMail import Email
import Wm_UI.readConfig as RC

readConfig = RC.ReadConfig()

class ExecuteCase(object):

    def __init__(self):

        self.Msg_Title = readConfig.getMail('Msg_Title')
        self.casePath = os.path.join(RC.rootPath,'test_case')
        self.reportPath = os.path.join(RC.rootPath,'test_report')
        self.Text_description = readConfig.getMail('Text_description')
        self.on_off = readConfig.getMail('on-off')

    def exeCase(self):
        test_discover = unittest.defaultTestLoader.discover(self.casePath, pattern='test*.py')
        now = time.strftime("%Y-%m-%d-%H_%M_%S")
        filename = self.reportPath + r'\result-' + now + '.html'
        print filename
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title=self.Msg_Title, description=self.Text_description)
        runner.run(test_discover)
        fp.close()
        self.sendEmail(filename)

    def sendEmail(self,filename):

        if self.on_off == 'on':
            sendMail = Email()
            mail = sendMail.sendEMail(filename)
            if mail:
                print("发送成功！")
            else:
                print("发送失败！")
        else:
            print '邮件未发送，如需发送邮件，请打开邮件发送开关！'


if __name__ == '__main__':

    caseExe = ExecuteCase()
    caseExe.exeCase()

