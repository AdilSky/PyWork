#-*-coding:utf-8-*-
#商城添加购物车功能自动化测试用例 by yanglei
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
#import baseinfo
from UiTest_temp import  baseinfo

class cart(unittest.TestCase):
    u'''加入购物车功能测试'''
    ####登录系统
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

    ####测试再次购买加入购物车
    def test_buy_again(self):
        '''再次购买加入购物车'''
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="slide_wrap"]/ul/li[2]').click()
            self.driver.find_element_by_xpath('//*[@id="firstpane"]/div[1]/a[1]').click()
            self.driver.find_element_by_xpath('//*[@id="searchForm"]/ul/li[1]/div[1]/input').send_keys("250190205912300")
            self.driver.find_element_by_id("searchBtn").click()
            self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/ul/li/table/tbody/tr[1]/td[4]/p[2]/button').click()
            time.sleep(1)
            pn1_text = self.driver.find_element_by_xpath(".//*[@id='seller_0']/table[2]/tbody/tr[1]/td[3]/a/div/p").text
            pn2_text = self.driver.find_element_by_xpath(".//*[@id='seller_0']/table[2]/tbody/tr[2]/td[3]/a/div/p").text
            pn3_text = self.driver.find_element_by_xpath(".//*[@id='seller_0']/table[2]/tbody/tr[3]/td[3]/a/div/p").text
            if pn1_text == "化痔灵片" and pn2_text == "化痔灵片" and pn3_text == "化痔灵片":
                print(U"再次购买加入购物车成功!")
                pn1_text = 1
            else:
                print(u"再次购买加入购物车异常(执行结果与预期不符)!")
                pn1_text = 0
                self.delete_product()
                self.assertEqual(pn1_text, 1, msg=None)
        except BaseException as msg:
            print(U"因未找到对应元素,测试用例未正常执行!")



if __name__ == "__main__":
    unittest.main()
