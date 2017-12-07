#-*-coding:utf-8-*-
# Time:2017/9/19 19:52
# Author:YangYangJun

import MySQLdb
import time

import baseinfo


host = baseinfo.myhost
user = baseinfo.myuser
passwd = baseinfo.mypasswd
db = baseinfo.mydb
port = baseinfo.myport




#建立连接

myConnect = MySQLdb.connect(host,user,passwd,db,port,charset= 'utf8')

#打开游标

myCursor = myConnect.cursor()

myselect = "select * from luckynumber where LID >= '%d'" %(24)

myCursor.execute(myselect)

result = myCursor.fetchone()
print result

#执行插入
create_time = time.strftime('%Y-%m-%d %H:%M:%S')
update_time = time.strftime('%Y-%m-%d %H:%M:%S')
name = '杨要军'
Remark = '测试数据'

myinsert= "insert into mytest(username,name,CreateTime,ModifyTime,Remark) " \
          "VALUES ('%s','%s','%s','%s','%s')" \
          %('Yang',name,create_time,update_time,Remark)

try:
    print "执行插入"
    exeinsert = myCursor.execute(myinsert)
    print exeinsert
    myConnect.commit()
except UnicodeEncodeError as e:
    #发生错误时回滚
    print '执行回滚'
    print e
    myConnect.rollback()

mytestsele = "select name  from mytest where id = '%d'" %(9)

myCursor.execute(mytestsele)

seleresult = myCursor.fetchone()
print seleresult
print "seleresult :%s" % seleresult


#执行更新

myupdate = "update mytest set name = '%s' where id > '%d' " %("李雷",9)

try:
    print "执行更新"
    myCursor.execute(myupdate)
    myConnect.commit()
except UnicodeEncodeError as e:
    print "执行回滚"
    print e
    myCursor.rollback()

mytestsele = "select name  from mytest where id = '%d'" %(10)

myCursor.execute(mytestsele)

seleresult = myCursor.fetchone()
print seleresult
print "seleresult :%s" % seleresult


#执行删除

mydelet = "delete  from mytest where id < '%d'" % (9)

try:
    print "执行删除"
    myCursor.execute(mydelet)
    myConnect.commit()
except UnicodeEncodeError as e:
    print "执行回滚"
    print e
    myCursor.rollback()

mytestsele = "select name  from mytest where id = '%d'" %(10)

myCursor.execute(mytestsele)

seleresult = myCursor.fetchone()
print seleresult
print "seleresult :%s" % seleresult

myConnect.close



