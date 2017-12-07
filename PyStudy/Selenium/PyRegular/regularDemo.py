#-*-coding:utf-8-*-
# Time:2017/10/1 7:26
# Author:YangYangJun

#正则表达式

import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
    print "matchObj.group(3) : ", matchObj.group(1,2)
else:
    print "No match!!"
#返回匹配对象的位置
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配（0,3）
print(re.match('com', 'www.runoob.com'))


print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配


# 将匹配的数字乘于 2
def double(matched):
    print "***"

    print matched
    value = int(matched.group())
    print value
    print matched.group('value')
    print value
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
print double
