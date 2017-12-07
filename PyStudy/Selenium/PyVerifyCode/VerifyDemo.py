#-*-coding:utf-8-*-
# Time:2017/9/29 7:16
# Author:YangYangJun
import time
from pytesseract import *

from selenium import webdriver

from PIL import Image, ImageEnhance

import baseinfo

url = baseinfo.url

driver = webdriver.Firefox()

driver.maximize_window()

driver.get(url)
time.sleep(3)
driver.save_screenshot('verifyCode.png')  #截取当前网页，该网页有我们需要的验证码
time.sleep(2)
#定位验证码
imgelement = driver.find_element_by_xpath(".//*[@id='imgObj']")
#获取验证码x,y轴坐标
location = imgelement.location
#获取验证码的长宽
size = imgelement.size
driver.quit()
#写成我们需要截取的位置坐标
rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
# 打开截图
i = Image.open('verifyCode.png')
#使用Image的crop函数，从截图中再次截取我们需要的区域
imgry=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域

imgry.save('getVerifyCode.png')

im=Image.open('getVerifyCode.png')

im = im.convert('L')#图像加强，二值化

sharpness =ImageEnhance.Contrast(im)#对比度增强

sharp_img = sharpness.enhance(2.0)

sharp_img.save("newVerifyCode.png")

newVerify = Image.open('newVerifyCode.png')

# 使用image_to_string识别验证码
text=image_to_string(newVerify).strip() #使用image_to_string识别验证码
#text1 = image_to_string('newVerifyCode.png').strip()
print text
#print text1





