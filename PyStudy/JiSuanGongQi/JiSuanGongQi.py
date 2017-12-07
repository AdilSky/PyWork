#-*-coding:utf-8-*-
# Time:2017/11/1 16:22
# Author:YangYangJun

import datetime



start = datetime.date(2017,3,28)
end = datetime.date(2017,11,15)

days = (end - start).days

weeks = days/7.0

yearholiday = (days/365.0)*5


print days
print weeks
print yearholiday
