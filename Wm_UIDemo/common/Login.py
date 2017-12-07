#-*-coding:utf-8-*-
# Time:2017/10/30 22:51
# Author:YangYangJun
from selenium.webdriver import ActionChains

from Wm_UIDemo import readConfig
from selenium import webdriver
import time

rC = readConfig.ReadConfig()

class MyLogin(object):

    def __init__(self):
        self.floatWindow = rC.getCaseSet('FloatWindow')
        pass

    def login(self,username,password):
        self.driver = webdriver.Firefox()
        self.base_url = rC.getHTTP('base_url')
        time.sleep(1)
        self.driver.maximize_window()
        self.driver.get("%s/user/tologin" % self.base_url)
        double_click = self.driver.find_element_by_id("username")
        ActionChains(self.driver).double_click(double_click).perform()
        self.driver.find_element_by_id("username").send_keys("%s" % username)
        double_click = self.driver.find_element_by_id("password")
        ActionChains(self.driver).double_click(double_click).perform()
        self.driver.find_element_by_id("password").send_keys("%s" % password)
        self.driver.find_element_by_id("sign_btn").click()
        print(u"登录成功")
        return self.driver
        pass

    def directLogin(self,username,password):
        '定义直连用户登录函数'


        # self.username = readConfig.getUserInfo('directName')
        # self.password = readConfig.getUserInfo('directPassword')
        #
        # self.driver = self.login(self.username,self.password)
        self.driver = self.login(username, password)
        floatWindow = self.floatWindow
        result = 'P'
        if floatWindow == 'on':
            print '活动期间打开悬浮窗口'
            #关闭悬浮窗口
            self.driver.find_element_by_id("aug_lead_close").click()
            self.driver.quit()
            return result
        else:
            self.driver.quit()
            return result



if __name__ == '__main__':
    pass
