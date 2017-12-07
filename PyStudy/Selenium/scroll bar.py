#-*-coding:utf-8-*-
# Time:2017/8/24 17:44
# Author:YangYangJun

from selenium import webdriver

class ScrollControl(object):

    def __init__(self,driver,base_url):

        #driver = webdriver.Firefox()
        driver = webdriver.Chrome()
        driver.get('http://www.hao123.com/')
        name = driver.name
        print  name


    #回到浏览器底部
    def scroll_foot(self):
        if self.name == 'chrome':
            # chrome 使用该方式
            js = "var q=document.body.scrollTop=10000"
        else:
            # 其他浏览器使用这种方式
            js = "var q=document.body.scrollTop=10000"
        return self.driver.execute_script(js)

    #回到浏览器顶部
    def scroll_top(self):
        if self.name == 'chrome':
            js = "var q=document.body.scrollTop=0"
        else:
            js = "var q=document.documentElement.scrollTop=0"
        return self.driver.execute_script(js)



