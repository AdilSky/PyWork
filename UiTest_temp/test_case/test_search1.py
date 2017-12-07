#-*-coding:utf-8-*-#商城搜索功能自动化测试用例 by yangleiimport sysreload(sys)sys.setdefaultencoding('utf8')from selenium import webdriverimport timeimport unittestfrom selenium.webdriver.common.action_chains import ActionChains#import baseinfofrom UiTest import baseinfofrom selenium.webdriver.common.keys import Keysclass search(unittest.TestCase):    u'''搜索功能测试'''    ####登录系统    @ classmethod    def setUpClass(self):        self.base_url = baseinfo.base_url        self.username = baseinfo.undirect_username        self.password = baseinfo.undirect_password        self.driver = webdriver.Firefox()        time.sleep(1)        self.driver.maximize_window()        self.driver.get("%s/user/tologin" % self.base_url)        double_click = self.driver.find_element_by_id("username")        ActionChains(self.driver).double_click(double_click).perform()        self.driver.find_element_by_id("username").send_keys("%s" % self.username)        double_click = self.driver.find_element_by_id("password")        ActionChains(self.driver).double_click(double_click).perform()        self.driver.find_element_by_id("password").send_keys("%s" % self.password)        self.driver.find_element_by_id("sign_btn").click()        print(u"登录成功")    @ classmethod    def tearDownClass(self):        time.sleep(1)        self.driver.quit()    def test_accept_search(self):         '''国药准字号搜索'''         try:            time.sleep(1)            self.driver.find_element_by_id("keywordInput").clear()            time.sleep(2)            self.driver.find_element_by_id("keywordInput").send_keys(u"国药准字Z41021116")            self.driver.find_element_by_id("header_search_btn").click()            self.driver.find_element_by_xpath('//*[@id="search_result_list"]/li/div/table/tbody/tr[2]/td[9]/p/a').click()            time.sleep(1)            #切换窗口            handleList = self.driver.window_handles            self.driver.switch_to.window(handleList[-1])            time.sleep(1)            #将页面滚动动条拖到底部            js = "var q=document.documentElement.scrollTop=10000"            self.driver.execute_script(js)            time.sleep(1)            get_text = self.driver.find_element_by_xpath(".//*[@id='send']/div/table/tbody/tr[12]/td[2]").text            if get_text == "国药准字Z41021116":                print(u"国药准字号搜索成功")                get_text = 1            else:                print(u"国药准字号搜索失败")                get_text = 0                self.assertEqual(get_text, 1, msg=None)         except BaseException as msg:             print(U"因未找到对应元素,测试用例未正常执行!")             print msg         finally:             self.driver.switch_to.window(handleList[0])    def test_bname_search(self):        '''通用名搜索'''        try:            time.sleep(1)            self.driver.find_element_by_id("keywordInput").clear()            time.sleep(2)            self.driver.find_element_by_id("keywordInput").send_keys(u"大山楂丸")            self.driver.find_element_by_id("header_search_btn").click()            self.driver.find_element_by_xpath('//*[@id="search_result_list"]/li/div/table/tbody/tr[2]/td[9]/p/a').click()            time.sleep(1)            #切换窗口            handleList = self.driver.window_handles            self.driver.switch_to.window(handleList[-1])            name_text = self.driver.find_element_by_xpath(".//*[@id='goods_name']").text            if name_text == "大山楂丸":                print (u"通用名搜索成功")                name_text = 1            else:                print (u"通用名搜索失败")                name_text = 0                self.assertEqual(name_text, 1, msg=None)        finally:            self.driver.switch_to.window(handleList[0])    def test_cbarcode_search(self):        '''条形码搜索'''        try:            time.sleep(1)            self.driver.find_element_by_id("keywordInput").clear()            time.sleep(2)            self.driver.find_element_by_id("keywordInput").send_keys(u"6921578753874")            self.driver.find_element_by_id("header_search_btn").click()            time.sleep(1)            bar_text = self.driver.find_element_by_xpath(".//*[@id='search_result_list']/li/table/tbody/tr/td[3]/p").text            if bar_text == "洛阳顺势药业有限公司":                print (u"条形码搜索成功")                bar_text = 1            else:                print (u"条形码搜索失败")                bar_text = 0                self.assertEqual(bar_text, 1, msg=None)        except BaseException as msg:            print "未找到页面元素！"            print msg    def test_dzjm_search(self):        '''助记码搜索'''        try:            time.sleep(1)            self.driver.find_element_by_id("keywordInput").clear()            time.sleep(2)            self.driver.find_element_by_id("keywordInput").send_keys(u"dszw")            self.driver.find_element_by_id("header_search_btn").click()            time.sleep(1)            zjm_text = self.driver.find_element_by_xpath(".//*[@id='search_result_list']/li/table/tbody/tr/td[3]/p").text            if zjm_text == "洛阳顺势药业有限公司":                print (u"助记码搜索成功")                zjm_text = 1            else:                print (u"助记码搜索失败")                zjm_text = 0                self.assertEqual(zjm_text, 1, msg=None)        except BaseException as msg:            print "未找到页面元素！"            print msg    def test_efactory_search(self):        '''生产厂家搜索'''        try:            time.sleep(1)            self.driver.find_element_by_id("keywordInput").clear()            time.sleep(2)            self.driver.find_element_by_id("keywordInput").send_keys(u"洛阳顺势药业有限公司")            self.driver.find_element_by_id("header_search_btn").click()            self.driver.find_element_by_xpath(".//*[@id='search_result_list']/li[1]/div/table/tbody/tr[1]/td[9]/p/a").click()            time.sleep(1)            #切换到单店详情页            handleList = self.driver.window_handles            self.driver.switch_to.window(handleList[-1])            fac_text = self.driver.find_element_by_xpath(".//*[@id='shop_goods']/div[2]/div[1]/form/ul/li[5]/ul/li[5]").text            if "洛阳顺势药业有限公司" in fac_text:                print (u"生产厂家搜索成功")                get_text = 1            else:                print (u"生产厂家搜索失败")                get_text = 0                self.assertEqual(get_text, 1, msg=None)        finally:            self.driver.switch_to.window(handleList[0])    def test_fpromotion_search(self):        '''促销商品搜索'''        try:            time.sleep(1)            # 全部商品分类            self.driver.find_element_by_xpath(".//*[@id='header_all_classify']/span").click()            time.sleep(1)            # 筛选促销商品            self.driver.find_element_by_xpath(".//*[@id='other_checkbox']/label[2]/i").click()            time.sleep(3)            fac_list = self.driver.find_elements_by_css_selector(".w220.ellipsis")            for fac in fac_list:                if fac.text == u'洛阳顺势药业有限公司':                    i = fac_list.index(fac)                    print i                    i = i + 1                    break            print i            googs_path = ".//*[@id='search_result_list']/li[%d]/div/table/tbody/tr[1]/td[9]/p/a" % i            time.sleep(5)            self.driver.find_element_by_xpath(googs_path).click()            # 切换到单店详情页            handleList = self.driver.window_handles            self.driver.switch_to.window(handleList[-1])            time.sleep(5)            pro_text = self.driver.find_element_by_xpath(                ".//*[@id='shop_goods']/div[2]/div[1]/form/ul/li[3]/div[2]/span").text            if pro_text == "促销":                print (u"促销商品搜索成功")                pro_text = 1            else:                print (u"促销商品搜索失败")                pro_text = 0                self.assertEqual(pro_text, 1, msg=None)        finally:            self.driver.switch_to.window(handleList[0])    def test_gscore_search(self):        '''鹅蛋商品搜索'''        try:            time.sleep(3)            # 点击所有商品            self.driver.find_element_by_xpath(".//*[@id='search_filter']/li[1]/span").click()            # 筛选鹅蛋商品            self.driver.find_element_by_xpath(".//*[@id='other_checkbox']/label[1]/i").click()            time.sleep(1)            self.driver.find_element_by_xpath(".//*[@id='search_result_list']/li[1]/div/table/tbody/tr[1]/td[9]/p/a").click()            # 切换到单店详情页            handleList = self.driver.window_handles            self.driver.switch_to.window(handleList[-1])            sco_text = self.driver.find_element_by_xpath(".//*[@id='shop_goods']/div[2]/div[1]/form/ul/li[3]/div[1]/span").text            if sco_text == "鹅蛋":                print (u"鹅蛋商品搜索成功")                sco_text = 1            else:                print (u"鹅蛋商品搜索失败")                sco_text = 0                self.assertEqual(sco_text, 1, msg=None)        except BaseException as msg:            print(U"因未找到对应元素,测试用例未正常执行!")            print msg        finally:            self.driver.switch_to.window(handleList[0])if __name__ == "__main__":    unittest.main()