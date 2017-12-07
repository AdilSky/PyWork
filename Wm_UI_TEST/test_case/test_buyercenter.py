#-*-coding:utf-8-*-
#商城买家中心功能自动化测试用例
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import baseinfo
#from Wm_UI import  baseinfo

class buyercenter(unittest.TestCase):
    '''买家中心功能测试'''
    @ classmethod
    def setUpClass(self):
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

    @ classmethod
    def tearDownClass(self):
        time.sleep(1)
        self.driver.quit()

    def test_buyercenter(self):
        '''进入买家中心'''
        try:
            time.sleep(1)
            #点击侧边栏上的买家中心，进入买家中心
            self.driver.find_element_by_xpath('//*[@id="slide_wrap"]/ul/li[2]').click()
            #判断进户买家中心
            buyer_text = self.driver.find_element_by_xpath('/html/body/div[2]/div/span').text
            if buyer_text == "买家中心":
                print(U"非直连用户进入买家中心正常!")
                buyer_text = 1
            else:
                print(U"非直连用户进入买家中心异常(执行结果与预期不符)!")
                buyer_text = 0
            self.assertEqual(buyer_text, 1, msg=None)
            time.sleep(1)
            #点击左侧菜单，进入订单管理
            self.driver.find_element_by_xpath('//*[@id="firstpane"]/div[1]/a[1]').click()
            #判断进户订单管理
            order_text = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/span').text
            if order_text == "订单管理":
                print(U"非直连用户进入订单管理正常!")
                order_text = 1
            else:
                print(U"非直连用户进入订单管理异常(执行结果与预期不符)!")
                order_text = 0
                self.assertEqual(order_text, 1, msg=None)
            #点击查看详情，进入订单详情页
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/ul/li[1]/table/tbody/tr[1]/td[3]/a').click()
            #获取订单管理页窗口句柄
            order_windows = self.driver.current_window_handle
            #获取当前所有打开的窗口句柄
            all_handles = self.driver.window_handles
            #切换到当前订单详情页
            for detail_handle in all_handles:
                if detail_handle != order_windows:
                    self.driver.switch_to.window(detail_handle)
                    phone_text = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/ul/li[1]/div[1]/p[2]').text
                    if phone_text == "联系电话：15201062199":
                        print(U"非直连用户进入订单详情页正常!")
                    else:
                        print(U"非直连用户进入订单详情页异常(执行结果与预期不符)!")
        except BaseException as msg:
            print(U"因未找到对应元素,测试用例未正常执行!")
            print msg
            self.assertIsNone(msg, msg=None)

if __name__ == "__main__":
    unittest.main()
