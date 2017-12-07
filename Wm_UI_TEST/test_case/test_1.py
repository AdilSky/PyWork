# -*-coding:utf-8-*-
# 自动化测试初始化 by yanglei
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from Wm_UI_TEST import  baseinfo
#import baseinfo


class default(unittest.TestCase):
    '''自动化测试初始化'''

    # 非直连用户登录
    def undirectuser_login(self):
        '''非直连用户登录'''
        self.base_url = baseinfo.base_url
        self.username = baseinfo.undirect_username
        self.password = baseinfo.undirect_password
        self.driver = webdriver.Firefox()
        time.sleep(1)
        self.driver.maximize_window()
        self.driver.get("%s/user/tologin" % self.base_url)
        double_click = self.driver.find_element_by_id("username")
        ActionChains(self.driver).double_click(double_click).perform()
        self.driver.find_element_by_id("username").send_keys("%s" % self.username)
        double_click = self.driver.find_element_by_id("password")
        ActionChains(self.driver).double_click(double_click).perform()
        self.driver.find_element_by_id("password").send_keys("%s" % self.password)
        self.driver.find_element_by_id("sign_btn").click()
        print(u"登录成功")

    # 直连用户登录
    def directuser_login(self):
        '''直连用户登录'''
        self.base_url = baseinfo.base_url
        self.username = baseinfo.direct_username
        self.password = baseinfo.direct_password
        self.driver = webdriver.Firefox()
        time.sleep(1)
        self.driver.maximize_window()
        self.driver.get("%s/user/tologin" % self.base_url)
        double_click = self.driver.find_element_by_id("username")
        ActionChains(self.driver).double_click(double_click).perform()
        self.driver.find_element_by_id("username").send_keys("%s" % self.username)
        double_click = self.driver.find_element_by_id("password")
        ActionChains(self.driver).double_click(double_click).perform()
        self.driver.find_element_by_id("password").send_keys("%s" % self.password)
        self.driver.find_element_by_id("sign_btn").click()
        print(u"登录成功")
        time.sleep(2)
        # 关闭悬浮窗口
        self.driver.find_element_by_id("aug_lead_close").click()

    # 判断用户是否登录成功
    def islogin(self):
        loginstate = 0
        try:
            self.driver.find_element_by_id("loginOut")
        except Exception:
            loginstate = 1
        self.assertEqual(loginstate, 0, msg="username or password is not correct")
        if loginstate == 1:
            self.driver.quit()

            # 非直连用户购物车初始化

    def test_undirectuser_clean_cart(self):
        '''非直连用户购物车初始化'''
        try:
            self.undirectuser_login()
            time.sleep(1)
            # 判断用户登录成功
            self.islogin()
            cartNum = self.driver.find_element_by_id('cly_cart_total').text
            if int(cartNum) != 0:
                # 点击侧边栏上的购物车，进入购物车
                self.driver.find_element_by_xpath('//*[@id="slide_wrap"]/ul/li[4]').click()
                # 点击全部删除
                self.driver.find_element_by_class_name('del-shopping').find_elements_by_tag_name('button')[1].click()
                # 弹出的确认框，点击确认
                self.driver.find_element_by_xpath('//*[@id="popup_confirm"]/div[1]/div[3]/button[1]').click()
                time.sleep(2)
                warn_text = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/p[1]/strong').text
                if warn_text == "您的购物车还是空的，赶紧行动吧！":
                    print(U"非直连用户测试数据初始化正常!")
                    warn_text = 1
                else:
                    print(U"非直连用户测试数据初始化异常(执行结果与预期不符)!")
                    warn_text = 0
                self.assertEqual(warn_text, 1, msg=None)
            else:
                print(U"非直连用户测试数据初始化完成")
        except BaseException as msg:
            print(U"因未找到对应元素,测试用例未正常执行!")
            print msg
            self.assertIsNone(msg, msg=None)
        finally:
            self.driver.quit()
            # 直连用户购物车初始化

    def test_directuser_clean_cart(self):
        '''直连用户购物车初始化'''
        try:
            self.directuser_login()
            time.sleep(1)
            # 判断用户登录成功
            self.islogin()
            cartNum = self.driver.find_element_by_id('cly_cart_total').text
            time.sleep(1)
            print cartNum
            if int(cartNum) != 0:
                # 点击侧边栏上的购物车，进入购物车
                time.sleep(1)
                self.driver.find_element_by_xpath(".//*[@id='slide_wrap']/ul/li[4]/p[1]").click()
                time.sleep(2)



                cartNum = int(cartNum)
                cartNum = cartNum + 1
                print cartNum
                for i in range(1,cartNum):
                    print i

                # 点击全部删除
                self.driver.find_element_by_xpath(".//*[@id='shopping_bot_wrap']/div/div[2]/div[1]/button[2]").click()
                time.sleep(2)
                # 弹出的确认框，点击确认
                self.driver.find_element_by_xpath('//*[@id="popup_confirm"]/div[1]/div[3]/button[1]').click()
                time.sleep(2)
                warn_text = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/p[1]/strong').text
                if warn_text == "您的购物车还是空的，赶紧行动吧！":
                    print(U"直连用户测试数据初始化正常!")
                    warn_text = 1
                else:
                    print(U"直连用户测试数据初始化异常(执行结果与预期不符)!")
                    warn_text = 0
                self.assertEqual(warn_text, 1, msg=None)
            else:
                print(U"直连用户测试数据初始化完成")
        except BaseException as msg:
            print(U"因未找到对应元素,测试用例未正常执行!")
            print msg
            self.assertIsNone(msg, msg=None)
        finally:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()

