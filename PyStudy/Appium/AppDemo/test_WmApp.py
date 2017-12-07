#-*-coding:utf-8-*-
#Time:2017/7/21 16:32
#Author:YangYangJun


import time
import unittest

from appium import webdriver

import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Login(unittest.TestCase):

    def setUp(self):
        self.desired_caps = {}

        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '6.0'
        self.desired_caps['deviceName'] = 'N79SIV5PVCSODAQC'
        self.desired_caps['appPackage'] = 'com.hpf911.mrg'
        self.desired_caps['appActivity'] = 'com.uzmap.pkg.EntranceActivity'
        self.desired_caps['unicodeKeyboard'] = True
        self.desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        #self.driver.implicitly_wait(15)



    #测试异常登录-用户不存在

    def test_aNoUserLogin(self):

        driver  = self.driver
        time.sleep(5)
        driver.find_element_by_accessibility_id(u"我的").click()

        time.sleep(5)

        driver.find_element_by_accessibility_id(u"登录/注册").click()
        time.sleep(2)

        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("username")').clear()

        time.sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("username")').send_keys('xzbuyer1')
        time.sleep(2)

        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("password")').clear()

        time.sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("password")').send_keys('111111')

        time.sleep(2)

        driver.find_element_by_accessibility_id(u"登录").click()
        time.sleep(18)

        get_alertMessage = driver.find_elements_by_android_uiautomator('new Uiselector().resourceId("android:id/message")').get_attribute('name')
        time.sleep(2)
        if get_alertMessage == u'用户不存在':
            print u"用户不存在,用例执行成功！"
        else:
            print u"用例执行失败！"


    def test_bNoPassLogin(self):

        driver  = self.driver
        time.sleep(5)
        driver.find_element_by_accessibility_id(u"我的").click()

        time.sleep(5)

        driver.find_element_by_accessibility_id(u"登录/注册").click()
        time.sleep(2)

        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("username")').clear()

        time.sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("username")').send_keys('xzbuyer')
        time.sleep(2)

        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("password")').clear()

        time.sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("password")').send_keys('1111112')

        time.sleep(2)

        driver.find_element_by_accessibility_id(u"登录").click()
        time.sleep(18)

        get_alertMessage = driver.find_elements_by_android_uiautomator('new Uiselector().resourceId("android:id/message")').get_attribute('name')
        time.sleep(2)
        print get_alertMessage[0:5]

        # if get_alertMessage == u'用户不存在':
        #     print u"用户不存在,用例执行成功！"
        # else:
        #     print u"用例执行失败！"
        #

    # 测试正常登录

    def test_cLogin(self):

        driver = self.driver
        time.sleep(5)
        driver.find_element_by_accessibility_id(u"我的").click()

        time.sleep(5)

        driver.find_element_by_accessibility_id(u"登录/注册").click()
        time.sleep(2)

        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("username")').clear()

        time.sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("username")').send_keys('xzbuyer')
        time.sleep(2)

        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("password")').clear()

        time.sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("password")').send_keys('111111')

        time.sleep(2)

        driver.find_element_by_accessibility_id(u"登录").click()
        time.sleep(2)

        # 判断是否登录成功

        print driver.find_element_by_accessibility_id(u"西藏医药销售有限公司").get_attribute('name')

        nickName = driver.find_element_by_accessibility_id(u"西藏医药销售有限公司").get_attribute('name')
        temp = nickName[0:2]
        print  temp
        if nickName == u'西藏医药销售有限公司':
            print '登录成功！'

        else:
            print '登录失败！'

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()