#-*-coding:utf-8-*-
# Time:2017/8/24 20:37
# Author:YangYangJun


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Page(object):

    '''
    基础类，用于页面对象类的继承
    '''

    login_url = 'http://www.hao123.com'

    def __init__(self,sele_driver,base_url = login_url):
        self.base_url = base_url
        self.driver = sele_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url ==

