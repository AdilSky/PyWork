#-*-coding:utf-8-*-
#商城单店功能自动化测试用例
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import baseinfo
#from Wm_UI import  baseinfo
class sellershop(unittest.TestCase):
    '''单店功能测试'''
    ####登录系统
    @ classmethod
    def setUpClass(self):
        self.base_url = baseinfo.base_url
        self.username = baseinfo.sellerName
        self.password = baseinfo.sellerPassword
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

    def test_recommend(self):
        '''单店店铺推荐商品'''
        try:
            #进入卖家中心
            time.sleep(1)
            self.driver.find_element_by_xpath(".//*[@id='slide_wrap']/ul/li[2]").click()
            time.sleep(1)
            #点击店铺管理
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/h3[3]').click()
            time.sleep(1)
            #点击左侧栏商品推荐页
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[3]/a[3]').click()
            time.sleep(1)
            #推荐商品
            self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/form/table/tbody/tr[1]/td[7]/button').click()
            #弹出的确认框，点击确认
            self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[3]/button[1]').click()
            #进入单店页
            self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/form/table/tbody/tr[1]/td[2]/a/span/img').click()
            #获取搜索页窗口句柄
            recommend_windows = self.driver.current_window_handle
            #获取当前所有打开的窗口句柄
            all_handles = self.driver.window_handles
            #切换到单店详情页
            for shop_handle in all_handles:
                if shop_handle != recommend_windows:
                    self.driver.switch_to.window(shop_handle)
                    #点击首页
                    self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/ul/li[1]/a').click()
                    time.sleep(1)
                    recommend_text = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/ul/li').text
                    if recommend_text != "":
                        print(u"店铺推荐商品成功")
                        recommend_text = 1
                    else:
                        print(u"店铺推荐商品失败")
                        recommend_text = 0
                        self.assertEqual(recommend_text, 1, msg=None)
            #以下为取消推荐商品操作
            time.sleep(1)
            #进入卖家中心
            self.driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]').click()
            time.sleep(1)
            #点击店铺管理
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/h3[3]').click()
            time.sleep(1)
            #进入商品推荐页
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[3]/a[3]').click()
            time.sleep(1)
            #取消推荐商品
            self.driver.find_element_by_xpath(".//*[@id='productList']/table/tbody/tr[1]/td[7]/button").click()
            time.sleep(1)
            #弹出的确认框，点击确认
            self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[3]/button[1]').click()
            print(U"取消推荐商品成功")
        except BaseException as msg:
            print(U"因未找到对应元素,测试用例未正常执行!")
            print msg
            self.assertIsNone(msg, msg=None)

    def test_recommends(self):
        '''批量推荐商品'''
        try:
            #点击卖家中心首页
            time.sleep(1)
            self.driver.find_element_by_xpath(".//*[@id='float']/a").click()
            time.sleep(1)
            #点击店铺管理
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/h3[3]').click()
            time.sleep(1)
            #点击左侧栏商品推荐页
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[3]/a[3]').click()
            time.sleep(1)
            #全选（当页所有）
            self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]/span[1]/label/input').click()
            #把页面上最后 1 个 checkbox 勾去掉
            self.driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
            print(U"可推荐19个商品")
            #点击批量推荐按钮
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/span/input[1]').click()
            #弹出的确认框，点击确认
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[3]/button[1]').click()
            #text_text = u"未推荐"
            recommend_text = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/form/table/tbody/tr[1]/td[6]').text
            #self.assertEqual(recommend_text, text_text, msg="批量推荐商品失败，未找到对应元素！")
            if recommend_text == "未推荐":
                print(u"批量推荐成功")
                recommend_text = 1
            else:
                print(u"批量推荐失败")
                recommend_text = 0
                self.assertEqual(recommend_text, 1, msg=None)

            #以下为批量取消推荐操作
            time.sleep(1)
            #全选（当页所有）
            self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]/span[1]/label/input').click()
            #点击批量取消推荐按钮
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/span/input[2]').click()
            #弹出的确认框，点击确认
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[3]/button[1]').click()


        except BaseException as msg:
            print(U"因未找到对应元素，测试用例未正常执行！")
            print msg
            self.assertIsNone(msg, msg=None)


if __name__ == "__main__":
    unittest.main()
