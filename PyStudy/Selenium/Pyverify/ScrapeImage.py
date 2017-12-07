#-*-coding:utf-8-*-
# Time:2017/9/29 15:41
# Author:YangYangJun

import requests
import random
from urllib3 import request
t1 = random.randint(800,900)
print t1
data = {'t':t1}
host_url = 'http://kmustjwcxk3.kmust.edu.cn/jwweb/'
captcha_url = host_url+'sys/ValidateCode.aspx'
requests.urlretrieve(captcha_url,'12.jpg')

#print requests.post(captcha_url,data).text




