# -*-coding:utf-8-*-
# 商城下订单流程自动化测试用例 by yanglei
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
import time
import unittest
import baseinfo
from selenium.webdriver.common.action_chains import ActionChains

class order(unittest.TestCase):
    '''下订单功能测试'''
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

    # 非直连订单下单
    def test_undirect_order(self):
        '''非直连订单下单,立即购买,订单管理页,订单详情页'''
        try:
            self.undirectuser_login()
            time.sleep(1)
            # 判断用户登录成功
            self.islogin()
            # 搜索商品，添加到购物车
            self.driver.find_element_by_id("keywordInput").send_keys(u"化痔灵片")
            self.driver.find_element_by_id("header_search_btn").click()
            time.sleep(1)
            # 按价格排序
            self.driver.find_element_by_xpath(".//*[@id='sort_ul']/li[3]").click()
            # 单店详情页
            time.sleep(1)
            self.driver.find_element_by_xpath(".//*[@id='search_result_list']/tr[1]/td[1]/a/div[2]/p[1]").click()
            # 切换窗口
            handleList = self.driver.window_handles
            self.driver.switch_to.window(handleList[-1])
            warn_text = self.driver.find_element_by_xpath(".//*[@id='goods_name']").text
            if warn_text == "化痔灵片":
                # 选择其他包装
                self.driver.find_element_by_xpath(".//*[@id='pack_list']/span[2]").click()
                self.driver.find_element_by_xpath(".//*[@id='action_event_box']/button[1]").click()
                time.sleep(1)
                self.driver.find_element_by_xpath(".//*[@id='submit_order']").click()
                print (U"立即购买，订单提交成功！")
                warn_text = 1
            else:
                print (U"进入单店失败，无法立即购买！")
                warn_text = 0
                self.assertEqual(warn_text, 1, msg=None)
            self.driver.switch_to.window(handleList[0])
            # 搜索结果页加购物车
            time.sleep(1)
            self.driver.find_element_by_xpath(".//*[@id='search_result_list']/tr[1]/td[10]/button").click()
            self.driver.find_element_by_xpath(".//*[@id='slide_wrap']/ul/li[4]").click()
            handleList = self.driver.window_handles
            self.driver.switch_to.window(handleList[-1])
            # 生成订单
            self.driver.find_element_by_xpath(".//*[@id='shopping_bot_wrap']/div/div[2]/div[2]/button").click()
            time.sleep(1)
            # 买家留言
            self.driver.find_element_by_xpath(".//*[@id='cly_order_list']/li/div/div[1]/textarea").send_keys(u"~~测试订单")
            time.sleep(1)
            # 提交订单
            self.driver.find_element_by_xpath(".//*[@id='submit_order']").click()
            time.sleep(1)
            warn1_text = self.driver.find_element_by_xpath(".//*[@id='order_submit_success']/div[1]/div/p[1]/strong").text
            if warn1_text == "您的订单已提交成功，请耐心等待卖家发货！":
                print (U"非直连订单提交成功！")
                warn1_text = 1
            else:
                print (U"非直连订单提交失败！")
                warn1_text = 0
                self.assertEqual(warn1_text, 1, msg=None)
            # 订单管理页
            time.sleep(1)
            self.driver.find_element_by_xpath(".//*[@id='orderDatiles']").click()
            # 订单详情页
            self.driver.find_element_by_xpath(".//*[@id='cly_order_list']/li[1]/table/tbody/tr/td[3]/a").click()
            handleList = self.driver.window_handles
            self.driver.switch_to.window(handleList[-1])
            phone_text = self.driver.find_element_by_xpath(".//*[@id='cly_body']/div[4]/div[2]/div[2]/div/div/div/ul/li[1]/div[1]/p[2]").text
            if phone_text == "联系电话：13691246595":
                print (U"非直连订单进入订单详情页成功！")
                phone_text = 1
            else:
                print (U"非直连订单进入订单详情页失败")
                phone_text = 0
                self.assertEqual(phone_text, 1, msg=None)
        except BaseException as msg:
            print(U"因未找到对应元素,测试用例未正常执行!")
            print msg
            self.assertIsNone(msg, msg=None)
        finally:
                self.driver.quit()

    # 直连订单下单
    def test_direct_order(self):
        '''直连订单下单,直连订单拆单'''
        try:
            self.directuser_login()
            time.sleep(1)
            # 判断用户登录是否成功
            self.islogin()
            time.sleep(1)
            # 搜索商品，添加到购物车
            self.driver.find_element_by_id("keywordInput").send_keys(u"鱼脑石")
            self.driver.find_element_by_id("header_search_btn").click()
            time.sleep(1)
            # 输入采购数量
            double_click = self.driver.find_element_by_xpath(".//*[@id='search_result_list']/tr/td[9]/div/input")
            ActionChains(self.driver).double_click(double_click).perform()
            self.driver.find_element_by_xpath(".//*[@id='search_result_list']/tr/td[9]/div/input").send_keys(u"4")
            time.sleep(1)
            self.driver.find_element_by_xpath(".//*[@id='search_result_list']/tr/td[10]/button").click()
            double_click = self.driver.find_element_by_id("keywordInput")
            ActionChains(self.driver).double_click(double_click).perform()
            self.driver.find_element_by_id("keywordInput").send_keys(u"生理性海水鼻腔护理液")
            self.driver.find_element_by_id("header_search_btn").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(".//*[@id='search_result_list']/tr/td[10]/button").click()
            self.driver.find_element_by_xpath('//*[@id="slide_wrap"]/ul/li[4]/p[1]').click()
            time.sleep(1)
            # 生成订单
            handleList = self.driver.window_handles
            self.driver.switch_to.window(handleList[-1])
            self.driver.find_element_by_xpath('//*[@id="shopping_bot_wrap"]/div/div[2]/div[2]/button').click()
            time.sleep(1)
            self.driver.find_element_by_id("submit_order").click()
            time.sleep(1)
            # 提交订单
            self.driver.find_element_by_id("orderDatiles").click()
            time.sleep(1)
            warn_test1 = self.driver.find_element_by_xpath(
                "/html/body/div[4]/div[1]/div/ul/li[1]/table/tbody/tr/td[1]/span[1]/a").text
            warn_test2 = self.driver.find_element_by_xpath(
                "/html/body/div[4]/div[1]/div/ul/li[2]/table/tbody/tr/td[1]/span[1]/a").text
            if warn_test1 == "生理性海水鼻腔护理液":
                if warn_test2 == "鱼脑石":
                    print(U"直连订单下单功能正常!")
                    print(U"直连订单拆单功能正常!")
                    warn_text = 1
                else:
                    print(U"直连订单下单功能异常(执行结果与预期不符)!")
                    warn_text = 0
                self.assertEqual(warn_text, 1, msg=None)
            else:
                if warn_test1 == "鱼脑石" and warn_test2 == "生理性海水鼻腔护理液":
                    print(U"直连订单下单功能正常!")
                    print(U"直连订单拆单功能正常!")
                    warn_text = 1
                else:
                    print(U"直连订单下单功能异常(执行结果与预期不符)!")
                    warn_text = 0
                self.assertEqual(warn_text, 1, msg=None)
        except BaseException as msg:
            print(U"因未找到对应元素,测试用例未正常执行!")
            print msg
            self.assertIsNone(msg, msg=None)
        finally:
            self.driver.quit()
if __name__ == "__main__":
    unittest.main()
