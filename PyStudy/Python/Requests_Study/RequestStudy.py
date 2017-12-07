#-*-coding:utf-8-*-
# Time:2017/10/11 22:53
# Author:YangYangJun

import requests

print requests

# requests.get()

#requests的介绍可以查看  D:/SProgram/Python/Lib/site-packages/requests/api.py 文件介绍

r = requests.get('http://zhengwu.beijing.gov.cn/jiedu/')

print r.text
print "--------*********---------"
print r.content

print "--------*********---------"

r = requests.post('http://zhengwu.beijing.gov.cn/jiedu/')

print r.text
print "--------*********---------"
print r.content






