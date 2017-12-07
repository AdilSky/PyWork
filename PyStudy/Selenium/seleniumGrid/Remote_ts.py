#-*-coding:utf-8-*-
# Time:2017/9/18 23:37
# Author:YangYangJun


from selenium import selenium
from selenium.webdriver import  Remote
import time

lists = {'http://localhost:4444/wd/hub':'chrome',
        'http://localhost:5555/wd/hub':'firefox'}


for host,browser in lists.items():
    print (host,browser)
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': browser,
                                          'version': '',
                                          'javascriptEnabled': True})

    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('remote')
    driver.find_element_by_id('su').click()
    time.sleep(5)
    driver.quit()



