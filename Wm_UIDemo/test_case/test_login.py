#-*-coding:utf-8-*-
# Time:2017/10/30 23:04
# Author:YangYangJun
import unittest



from Wm_UIDemo.common import Common

from Wm_UIDemo.common import Login

import Wm_UIDemo.readConfig as Rc

readConfig = Rc.ReadConfig()



class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.common = Common.Common()
        cls.login = Login.MyLogin()
        cls.directDataDic, cls.unDirectDataDic = cls.common.readExcel(xlsName='loginCase.xlsx', sheetName='Login', upList=[0,7,8])
        cls.getxlsData = cls.directDataDic
        print cls.directDataDic
        print cls.unDirectDataDic



    @classmethod
    def tearDownClass(cls):

        cls.common.writeExcel(xlsName='loginCase.xlsx', sheetName='Login', dataDic=cls.getxlsData, upList=[5, 6])
        #cls.driver.quit()
        pass



    def testDirectLogin(self):


        print self.getxlsData
        for i in self.getxlsData.keys():
            print i

            result = self.login.directLogin(self.getxlsData[i][2], self.getxlsData[i][3])



            if result == 'P':
                self.getxlsData[i][5]='seccess'
                self.getxlsData[i][6]='T'
            else:
                self.getxlsData[i][5] = 'failure'
                self.getxlsData[i][6] = 'F'


    # def testUnDirectLogin(self):
    #
    #     pass




# common = Common.Common()
#


#
# getxlsData = common.readExcel(xlsName='loginCase.xlsx',sheetName='Login',upList=[0,7])
#
#
#
# def testLogin(name,password):
#     base_url = readConfig.getHTTP('base_url')
#
#     # username = readConfig.getUserInfo('undirectName')
#     # password = readConfig.getUserInfo('undirectPassword')
#     driver = webdriver.Firefox()
#     time.sleep(1)
#     driver.maximize_window()
#     driver.get("%s/user/tologin" % base_url)
#     double_click = driver.find_element_by_id("username")
#     ActionChains(driver).double_click(double_click).perform()
#     driver.find_element_by_id("username").send_keys("%s" % name)
#     double_click = driver.find_element_by_id("password")
#     ActionChains(driver).double_click(double_click).perform()
#     driver.find_element_by_id("password").send_keys("%s" % password)
#     driver.find_element_by_id("sign_btn").click()
#     print(u"登录成功")
#     driver.quit()
#     return 'P'
#
#
#
#
# for i in getxlsData.keys():
#
#
#     result = testLogin(getxlsData[i][2],getxlsData[i][3])
#
#     if result == 'P':
#         getxlsData[i][5]='seccess'
#         getxlsData[i][6]='T'
#     else:
#         getxlsData[i][5] = 'failure'
#         getxlsData[i][6] = 'F'
#
#
#
#
#
# common.writeExcel(xlsName='loginCase.xlsx',sheetName='Login',dataDic=getxlsData,upList=[5,6])
#
#
#
#


if __name__ == '__main__':

    unittest.main()

