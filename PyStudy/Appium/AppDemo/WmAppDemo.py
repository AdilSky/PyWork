#-*-coding:utf-8-*-
#Time:2017/7/20 18:12
#Author:YangYangJun

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
time.sleep(3)
driver.find_element_by_accessibility_id(u"我的").click()
time.sleep(3)


get_act = driver.current_activity
print  get_act
driver.find_element_by_accessibility_id(u"登录/注册").click()
time.sleep(5)
scts = driver.current_activity
print scts
time.sleep(5)

driver.find_element_by_android_uiautomator('new UiSelector().resourceId("username")').clear()
#driver.find_element_by_id("username").clear()
time.sleep(8)
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("username")').send_keys('xzbuyer')

time.sleep(8)

#driver.find_element_by_id('password').clear()
#time.sleep(3)
#driver.find_element_by_id('password').send_keys("111111")

driver.find_element_by_android_uiautomator('new UiSelector().resourceId("password")').clear()
#driver.find_element_by_id("username").clear()
time.sleep(8)
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("password")').send_keys('111111')

time.sleep(3)

driver.find_element_by_accessibility_id(u"登录").click()

time.sleep(2)



#判断是否登录成功

print driver.find_element_by_accessibility_id(u"西藏医药销售有限公司").get_attribute('name')

nickName = driver.find_element_by_accessibility_id(u"西藏医药销售有限公司").get_attribute('name')

if nickName == u'西藏医药销售有限公司':
    print '登录成功！'

else:
    print '登录失败！'



