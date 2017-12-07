#-*-coding:utf-8-*-
#商城添加购物车功能自动化测试用例 by yanglei
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import baseinfo
#from Wm_UI import  baseinfo
from selenium.webdriver.common.keys import Keys
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

    ####购物车勾选商品删除
    def delete_product(self):

        self.driver.find_element_by_class_name('del-shopping').find_elements_by_tag_name('button')[0].click()
        #弹出的确认框，点击确认
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="popup_confirm"]/div[1]/div[3]/button[1]').click()
    ####清空购物车
    def test_clean_cart(self):
        '''清空购物车'''
        try:
            time.sleep(1)
            #搜索商品，添加到购物车
            self.driver.find_element_by_id("keywordInput").send_keys(u"化痔灵片")
            self.driver.find_element_by_id("header_search_btn").click()
            time.sleep(1)

            #修改1
            #self.driver.find_element_by_xpath('//*[@id="search_result_list"]/li[1]/div/table/tbody/tr[1]/td[9]/p/input').click()

            fac_list = self.driver.find_elements_by_css_selector(".w220.ellipsis")
            for fac in fac_list:
                if fac.text == u'山西仁源堂药业有限公司':
                    i = fac_list.index(fac)

                    i = i + 1
                    break

            if len(fac_list) == 1:
                googs_path = ".//*[@id='search_result_list']/li/div/table/tbody/tr[1]/td[9]/p/input"

            else:
                googs_path =  googs_path = ".//*[@id='search_result_list']/li[%d]/div/table/tbody/tr[1]/td[9]/p/input" % i


            self.driver.find_element_by_xpath(googs_path).click()
            #点击侧边栏上的购物车，进入购物车
            self.driver.find_element_by_xpath('//*[@id="slide_wrap"]/ul/li[4]').click()
            #点击全部删除
            self.driver.find_element_by_class_name('del-shopping').find_elements_by_tag_name('button')[1].click()
            #弹出的确认框，点击确认
            self.driver.find_element_by_xpath('//*[@id="popup_confirm"]/div[1]/div[3]/button[1]').click()
            time.sleep(1)
            warn_text = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/p[1]/strong').text
            if warn_text == "您的购物车还是空的，赶紧行动吧！":
               print(U"清空购物车功能正常!")
               warn_text = 1
            else:
               print(U"清空购物车功能异常(执行结果与预期不符)!")
               warn_text = 0
            self.assertEqual(warn_text, 1, msg=None)
        except BaseException as msg:
            print(U"因未找到对应元素,测试用例未正常执行!")
            print msg
            self.assertIsNone(msg, msg=None)

    ##搜索结果页加入购物车
    def test_search_to_cart(self):
        '''搜索结果页加入购物车'''
        try:
            time.sleep(1)
            #搜索商品，添加到购物车
            self.driver.find_element_by_id("keywordInput").clear()
            self.driver.find_element_by_id("keywordInput").send_keys(u"大山楂丸")
            self.driver.find_element_by_id("header_search_btn").click()
            time.sleep(2)
            #修改2
            #self.driver.find_element_by_xpath('//*[@id="search_result_list"]/li/div/table/tbody/tr[2]/td[9]/p/input').click()

            fac_list = self.driver.find_elements_by_css_selector(".w220.ellipsis")

            for fac in fac_list:
                if fac.text == u'洛阳顺势药业有限公司':
                    i = fac_list.index(fac)
                    i = i + 1
                    break

            if len(fac_list) == 1:
                googs_path = ".//*[@id='search_result_list']/li/div/table/tbody/tr/td[9]/p/input"

            else:
                googs_path = ".//*[@id='search_result_list']/li[%d]/div/table/tbody/tr[2]/td[9]/p/input" % i

            self.driver.find_element_by_xpath(googs_path).click()
            #点击侧边栏上的购物车，进入购物车
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="slide_wrap"]/ul/li[4]').click()
            #查找商品
            time.sleep(3)
            product_text = self.driver.find_element_by_xpath('//*[@id="cart_goods_list"]/ul/li/table[2]/tbody/tr/td[3]/a/div/p').text
            time.sleep(2)
            if product_text == "大山楂丸":
               print (U"搜索结果页加入购物车功能正常!")
               product_text = 1
            else:
               print (U"搜索结果页加入购物车功能异常(执行结果与预期不符)!")
               product_text = 0
            self.delete_product()
            self.assertEqual(product_text, 1, msg=None)
        except BaseException as msg:
            print(U"因未找到对应元素,测试用例未正常执行!")
            print msg
            self.assertIsNone(msg, msg=None)
    ####单店页加入购物车
    def test_shop_to_cart(self):
        '''单店页加入购物车'''
        try:
            time.sleep(1)
            #搜索商品，添加到购物车
            self.driver.find_element_by_id("keywordInput").clear()
            self.driver.find_element_by_id("keywordInput").send_keys(u"大山楂丸")
            self.driver.find_element_by_id("header_search_btn").click()
            time.sleep(1)
            #修改 3
            #self.driver.find_element_by_xpath('//*[@id="search_result_list"]/li/div/table/tbody/tr[2]/td[9]/p/a').click()

            fac_list = self.driver.find_elements_by_css_selector(".w220.ellipsis")
            for fac in fac_list:
                if fac.text == u'洛阳顺势药业有限公司':
                    i = fac_list.index(fac)
                    i = i + 1
                    break
            googs_path = ".//*[@id='search_result_list']/li[%d]/div/table/tbody/tr[2]/td[9]/p/a" % i
            self.driver.find_element_by_xpath(googs_path).click()
            #切换窗口到店单面
            handleList = self.driver.window_handles
            self.driver.switch_to.window(handleList[-1])
            time.sleep(1)
            self.driver.find_element_by_id("action_event_box").find_elements_by_tag_name('button')[1].click()
            time.sleep(1)
            self.driver.find_element_by_xpath(".//*[@id='slide_wrap']/ul/li[4]").click()
            time.sleep(1)
            product_text = self.driver.find_element_by_xpath(".//*[@id='seller_0']/table[2]/tbody/tr/td[3]/a/div/p").text
            if product_text == "大山楂丸":
               print (U"单店页加入购物车功能正常!")
               product_text = 1
            else:
               print (U"单店页加入购物车功能异常(执行结果与预期不符)!")
               product_text = 0
            self.delete_product()
            self.assertEqual(product_text, 1, msg=None)
        except BaseException as msg:
            print(U"因未找到对应元素,测试用例未正常执行!")
            print msg
            self.assertIsNone(msg, msg=None)
        finally:
            self.driver.switch_to.window(handleList[0])

    ####多店页加入购物车
    def test_shops_to_cart(self):
        '''多店页加入购物车'''
        try:
            time.sleep(1)
            double_click = self.driver.find_element_by_id("keywordInput")
            ActionChains(self.driver).double_click(double_click).perform()
            #键盘删除
            self.driver.find_element_by_id("keywordInput").send_keys(Keys.BACK_SPACE)
            #搜索商品，添加到购物车
            time.sleep(1)
            self.driver.find_element_by_id("keywordInput").clear()
            self.driver.find_element_by_id("keywordInput").send_keys(u"健胃止痛片")
            self.driver.find_element_by_id("header_search_btn").click()
            time.sleep(1)

            fac_list = self.driver.find_elements_by_css_selector(".w220.ellipsis")
            for fac in fac_list:
                if fac.text == u'河北百善药业有限公司':
                    i = fac_list.index(fac)
                    i = i + 1
                    break

            if len(fac_list) == 1:
                googs_path = ".//*[@id='search_result_list']/li/table/tbody/tr/td[1]/a/span[2]/span[1]"

            else:
                googs_path = ".//*[@id='search_result_list']/li[%d]/table/tbody/tr/td[1]/a/span[2]/span[1]" % i
            #进入多点页
            self.driver.find_element_by_xpath(googs_path).click()
            time.sleep(1)
            #切换到多店页
            handleList = self.driver.window_handles
            self.driver.switch_to.window(handleList[-1])
            time.sleep(1)
            goods_list = self.driver.find_elements_by_css_selector(".seller-name.ellipsis")

            for good in goods_list:
                if good.text == u'新疆制药厂':
                    j = goods_list.index(good)
                    j = j + 1
                    break
            if len(goods_list) == 1:
                goog_path = ".//*[@id='cly_seller_list']/tr/td[9]/p/input"

            else:
                goog_path = ".//*[@id='cly_seller_list']/tr[%d]/td[9]/p/input" % j

            self.driver.find_element_by_xpath(goog_path).click()
            time.sleep(1)

            self.driver.find_element_by_xpath('//*[@id="slide_wrap"]/ul/li[4]').click()
            #查找商品
            product_text = self.driver.find_element_by_xpath(".//*[@id='seller_0']/table[2]/tbody/tr/td[3]/a/div/p").text
            if product_text == "健胃止痛片":
                print (U"多店页加入购物车功能正常!")
                product_text = 1
            else:
                print (U"多店页加入购物车功能异常(执行结果与预期不符)!")
                product_text = 0
            self.delete_product()
            self.assertEqual(product_text, 1, msg=None)
        except BaseException as msg:
            print(U"因未找到对应元素,测试用例未正常执行!")
            print msg
            self.assertIsNone(msg, msg=None)
        finally:

            self.driver.switch_to.window(handleList[0])

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
            print msg
            self.assertIsNone(msg, msg=None)

if __name__ == "__main__":
    unittest.main()




