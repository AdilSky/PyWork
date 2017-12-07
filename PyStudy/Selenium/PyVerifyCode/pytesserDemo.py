#-*-coding:utf-8-*-
# Time:2017/9/29 7:16
# Author:YangYangJun




from selenium import webdriver
#import Image
from PIL import Image, ImageEnhance
import baseinfo
from pytesser import *

url = baseinfo.url

driver = webdriver.Firefox()

driver.maximize_window()

driver.get(url)

driver.save_screenshot('verifyCode.png')


imgelement = driver.find_element_by_xpath(".//*[@id='imgObj']")

location = imgelement.location
size = imgelement.size
driver.quit()
rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))

i = Image.open('verifyCode.png')

imgry=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
imgry.save('getVerifyCode.png')
im=Image.open('getVerifyCode.png')
img = im.convert('L')#图像加强，二值化
sharpness =ImageEnhance.Contrast(imgry)#对比度增强
sharp_img = sharpness.enhance(2.0)
sharp_img.save("newVerifyCode.png")
newVerify = Image.open('newVerifyCode.png')
text=image_file_to_string('newVerifyCode.png') #使用image_to_string识别验证码
print text




