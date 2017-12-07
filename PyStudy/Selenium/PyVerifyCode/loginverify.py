#-*-coding:utf-8-*-
# Time:2017/9/29 7:16
# Author:YangYangJun




import time
from pytesseract import *

from selenium import webdriver

from PIL import Image, ImageEnhance




im=Image.open('login.png')
img = im.convert('L')#图像加强，二值化
sharpness =ImageEnhance.Contrast(img)#对比度增强
sharp_img = sharpness.enhance(2.0)
sharp_img.save("newVerifyCode.png")
newVerify = Image.open('newVerifyCode.png')
text=image_to_string(newVerify).strip() #使用image_to_string识别验证码
print text

