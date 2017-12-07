#-*-coding:utf-8-*-
# Time:2017/10/5 15:58
# Author:YangYangJun

import requests


import time
import random
import hashlib


dicturl = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='

timestamp = int(time.time()*1000) + random.randint(0,10)

inText = raw_input("请输入要翻译的内容：")

print timestamp
print inText
u = 'fanyideskweb'
d = inText
f = str(timestamp)
c ="rY0D^0'nM0}g5Mm1z%1G4"

sign = hashlib.md5((u+d+f+c)).hexdigest()
print sign
data = {
'i':inText,
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt':timestamp,
'sign':sign,
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_CLICKBUTTION',
'typoResult':'true'
}

response = requests.post(dicturl,data=data)
print response
print response.content








