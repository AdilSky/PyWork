#-*-coding:utf-8-*-
# Time:2017/9/19 17:24
# Author:YangYangJun

import MySQLdb
import baseinfo

host = baseinfo.host
user = baseinfo.user
passwd = baseinfo.passwd
db = baseinfo.db
port = baseinfo.port
#charset = baseinfo.charset


#打开数据库连接
#此处要加上端口，port且值是整型，不必加引号，如果加引号，会报错:TypeError: an integer is required。如果数据库端口为：3306.则不必填写端口
#写法一:
#DbConnect = MySQLdb.connect(host="db1.dev1.yiyao.cc",user="mall_root",passwd="20151118",db="mall",port=13306,charset="utf8")

#写法二:

#DbConnect = MySQLdb.connect('db1.dev1.yiyao.cc','mall_root','20151118','mall',13306,'utf8')

#写法三：

DbConnect = MySQLdb.connect(host,user,passwd,db,port,charset= 'utf8')


#获取游标

Dbcursor = DbConnect.cursor()

#使用execute方法执行SQL语句
Dbcursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库。
data = Dbcursor.fetchone()

print "Database version : %s " % data

#执行查询订单状态

selSql = "select order_status from med_order where order_sn >= '%d'" %(249975503328700)

Dbcursor.execute(selSql)

order_status = Dbcursor.fetchone()

print "order_status : %s " % order_status

# 关闭数据库连接
DbConnect.close()
































