#-*-coding:utf-8-*-
#Time:2017/8/24 23:33
#Author:YangYangJun

from selenium import selenium

sel = selenium('192.168.10.112',6666,'firefox','http://www.hao123.com/')
sel.start()
sel.open('/')
sel.type('id=search-input','selenium grid')
sel.click("XPath=.//*[@id='search-form']/div[2]/input")
# sel.wait_for_page_to_load('30')
sel.stop()