#-*-coding:utf-8-*-
# Time:2017/9/29 0:01
# Author:YangYangJun


import pytesseract



from PIL import Image
image=Image.open('new.jpg')
print image
vcode=pytesseract.image_to_string(image)
print vcode
