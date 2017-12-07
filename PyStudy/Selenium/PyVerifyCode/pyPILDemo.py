#-*-coding:utf-8-*-
# Time:2017/9/29 12:49
# Author:YangYangJun


#-*-coding:utf-8-*-
# Time:2017/9/29 7:16
# Author:YangYangJun



import time
from pytesseract import *

from selenium import webdriver

from PIL import Image, ImageEnhance

import baseinfo



def binarizing(img,threshod):
    pixdata = img.load()
    w,h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x,y] < threshod:
                pixdata[x,y] = 0
            else:
                pixdata[x,y] = 255
    return img

def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img




if __name__ == '__main__':
    url = baseinfo.url

    driver = webdriver.Firefox()

    driver.maximize_window()

    driver.get(url)

    driver.save_screenshot('verifyCode.png')

    imgelement = driver.find_element_by_xpath(".//*[@id='imgObj']")

    location = imgelement.location
    size = imgelement.size
    driver.quit()
    rangle = (
    int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))

    i = Image.open('verifyCode.png')

    imgry = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    imgry.save('getVerifyCode.png')

    im = Image.open('getVerifyCode.png').convert("L")
    img = im.convert('L')  # 图像加强，二值化
    sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
    sharp_img = sharpness.enhance(2.0)
    sharp_img.save("newVerifyCode.png")


    images = Image.open('newVerifyCode.png').convert("L")
    ii = binarizing(images,170)

    iii = depoint(ii)


    text = image_to_string(iii)  # 使用image_to_string识别验证码

    print text





