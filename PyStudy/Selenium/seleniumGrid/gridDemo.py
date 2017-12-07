#-*-coding:utf-8-*-
#Time:2017/8/24 23:33
#Author:YangYangJun

from selenium import selenium
from selenium.webdriver import  Remote
import time

#
# driver = Remote(command_executor='http://localhost:4444/wd/hub',
#                 desired_capabilities={'platform':'ANY',
#                                       'browserName':'firefox',
#                                       'version':'',
#                                       'javascriptEnabled':True})

#
# driver = Remote(command_executor='http://192.168.10.105:6666/wd/hub',
#                 desired_capabilities={'platform':'ANY',
#                                       'browserName':'firefox',
#                                       'version':'',
#                                       'javascriptEnabled':True})

driver = Remote(command_executor='http://192.168.1.66:6666/wd/hub',
                desired_capabilities={'platform':'ANY',
                                      'browserName':'chrome',
                                      'version':'',
                                      'javascriptEnabled':True})

driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('remote')
driver.find_element_by_id('su').click()
time.sleep(5)
driver.quit()
