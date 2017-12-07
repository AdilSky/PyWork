#-*-coding:utf-8-*-
# Time:2017/9/24 13:48
# Author:YangYangJun

import urllib
import urllib2

#方式一
#urllib没有Request(url)方法
url = "http://www.baidu.com"
response = urllib.urlopen(url)
print response.read()

#方式二
request = urllib2.Request(url)
response2 = urllib2.urlopen(request)

print response2.read()



