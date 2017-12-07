#-*-coding:utf-8-*-
#Time:2017/7/20 18:06
#Author:YangYangJun
import time
from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'N79SIV5PVCSODAQC'
desired_caps['appPackage'] = 'com.sina.weibo'
desired_caps['appActivity'] = 'com.sina.weibo.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
time.sleep(3)
driver.quit()
