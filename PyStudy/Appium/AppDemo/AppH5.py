#-*-coding:utf-8-*-
# Time:2017/8/2 21:44
# Author:YangYangJun


import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'N79SIV5PVCSODAQC'
desired_caps['appPackage'] = 'com.hpf911.mrg'
desired_caps['appActivity'] = 'com.uzmap.pkg.EntranceActivity'

#隐藏键盘
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)


