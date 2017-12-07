#-*-coding:utf-8-*-
# Time:2017/9/1 21:27
# Author:YangYangJun



import os
import sys
import SendKeys
#from UiTest import baseinfo

reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import re


def add_Address():

    nameList = ['xzyc001','xzyc002','xzyc003','xzyc004','xzyc005','xzyc006','xzyc007','xzyc008','xzyc009','xzyc010','xzyc011','xzyc012','xzyc013','xzyc014','xzyc015','xzyc016','xzyc017','xzyc018','xzyc019','xzyc020','xzyc021','xzyc022','xzyc023','xzyc024','xzyc025','xzyc026','xzyc027','xzyc028','xzyc029','xzyc030','xzyc031','xzyc032','xzyc033','xzyc034','xzyc035','xzyc036','xzyc037','xzyc038','xzyc039','xzyc040','xzyc041','xzyc042','xzyc043','xzyc044','xzyc045','xzyc046','xzyc047','xzyc048','xzyc049','xzyc050','xzyc051','xzyc052','xzyc053','xzyc054','xzyc055','xzyc056','xzyc057','xzyc058','xzyc059','xzyc060','xzyc061','xzyc062','xzyc063','xzyc064','xzyc065','xzyc066','xzyc067','xzyc068','xzyc069','xzyc070','xzyc071','xzyc072','xzyc073','xzyc074','xzyc075','xzyc076','xzyc077','xzyc078','xzyc079','xzyc080','xzyc081','xzyc082','xzyc083','xzyc084','xzyc085','xzyc086','xzyc087','xzyc088','xzyc089','xzyc090','xzyc091','xzyc092','xzyc093','xzyc094','xzyc095','xzyc096','xzyc097','xzyc098','xzyc099','xzyc100','xzyc101','xzyc102','xzyc103','xzyc104','xzyc105','xzyc106','xzyc107','xzyc108','xzyc109','xzyc110','xzyc111','xzyc112','xzyc113','xzyc114','xzyc115','xzyc116','xzyc117','xzyc118','xzyc119','xzyc120','xzyc121','xzyc122','xzyc123','xzyc124','xzyc125','xzyc126','xzyc127','xzyc128','xzyc129','xzyc130','xzyc131','xzyc132','xzyc133','xzyc134','xzyc135','xzyc136','xzyc137','xzyc138','xzyc139','xzyc140','xzyc141','xzyc142','xzyc143','xzyc144','xzyc145','xzyc146','xzyc147','xzyc148','xzyc149','xzyc150','xzyc151','xzyc152','xzyc153','xzyc154','xzyc155','xzyc156','xzyc157','xzyc158','xzyc159','xzyc160','xzyc161','xzyc162','xzyc163','xzyc164','xzyc165','xzyc166','xzyc167','xzyc168','xzyc169','xzyc170','xzyc171','xzyc172','xzyc173','xzyc174','xzyc175','xzyc176','xzyc177','xzyc178','xzyc179','xzyc180','xzyc181','xzyc182','xzyc183','xzyc184','xzyc185','xzyc186','xzyc187','xzyc188','xzyc189','xzyc190','xzyc191','xzyc192','xzyc193','xzyc194','xzyc195','xzyc196','xzyc197','xzyc198','xzyc199','xzyc200']

    #nameList = ['xzbuyer']

    for userName in nameList:

        driver = webdriver.Firefox()

        i = nameList.index(userName)
        i = i+1
        i = '%03d' %i
        print i
        nickName = u"西藏压力测试买家%s"%i

        driver.get("http://www.yiyao.cc/user/tologin")

        driver.maximize_window()
        #登录
        driver.find_element_by_xpath(".//*[@id='username']").clear()

        driver.find_element_by_xpath(".//*[@id='username']").send_keys(userName)

        driver.find_element_by_xpath(".//*[@id='password']").clear()
        driver.find_element_by_xpath(".//*[@id='password']").send_keys('111111')
        time.sleep(2)
        driver.find_element_by_id("sign_btn").click()
        time.sleep(2)
        ###
        driver.find_element_by_xpath(".//*[@id='slide_wrap']/ul/li[2]").click()

        time.sleep(3)

        driver.find_element_by_xpath(".//*[@id='firstpane']/h3[3]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='firstpane']/div[3]/a[3]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='receiver']").send_keys(u"杨要军")
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='company']").send_keys(nickName)
        time.sleep(1)
        sl1 = Select(driver.find_element_by_id('cly_province'))
        sl1.select_by_value('110000')
        time.sleep(2)
        #cly_city

        sl1 = Select(driver.find_element_by_id('cly_city'))
        sl1.select_by_value('110100')
        time.sleep(2)
        #cly_district
        sl1 = Select(driver.find_element_by_id('cly_district'))
        sl1.select_by_value('110105')
        time.sleep(2)
        Address = u"康泰金融大厦%s楼"%i
        driver.find_element_by_id('address').send_keys(Address)
        time.sleep(1)
        driver.find_element_by_id('address_mobile').send_keys("15201062199")
        time.sleep(1)
        driver.find_element_by_id("cly_address_btn").click()
        time.sleep(1)
        driver.quit()


if __name__ == '__main__':
    add_Address()












