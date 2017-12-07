#-*-coding:utf-8-*-
# Time:2017/9/25 14:44
# Author:YangYangJun

# import urllib2
#
#
# url = 'http://www.okooo.com/jingcai/'
# request = urllib2.Request(url)
# response2 = urllib2.urlopen(request)
#
#
# html = response2.read()
#
#
# # html = html.decode("utf-8")
# print html

import requests

url = 'http://www.okooo.com/jingcai/'

html = requests.get(url)
print type(html)
#html = html.encoding('utf-8')

#requests  content 不报错可以使用。
content = html.content
content = content.decode('gbk').encode("utf-8")

print content

#
# html = html.text
# html = html.decode('gbk').encode('utf-8')
# print html
#这种方式报错
# Traceback (most recent call last):
#   File "D:/WorkSpace/Python/Study/Selenium/PyScrape/other/bbe.py", line 37, in <module>
#     html = html.decode('gbk').encode('utf-8')
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 204-235: ordinal not in range(128)
#
#





