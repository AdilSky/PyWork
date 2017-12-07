#-*-coding:utf-8-*-
# Time:2017/10/18 22:30
# Author:YangYangJun

# 首先导入 ConfigParser 模块

import ConfigParser

# 这里发现 上面这种大写与下面的小写都可以，只是导入的时候是如何写的，下面实例化的时候就如何写。

# import configparser

configFile = 'testconfig.ini'


# 1、创建ConfigParser 实例

config = ConfigParser.ConfigParser()

# 2、读取配置文件

config.read(configFile)

# 3、获取配置文件的章节序列

print config.sections()  # ['DATABASE']


# 4、获取配置文件中对应章节所有键的序列

print config.options('DATABASE')  # ['host', 'username', 'password', 'port', 'database']

# 5、获取配置文件中对应章节 对应键的值

print config.get('DATABASE','host') # 50.23.190.57


# 6、获取配置文件中对应章节的所有键值对

print config.items('DATABASE')  # [('host', '50.23.190.57'), ('username', 'TestYang'), ('password', 'TestYang'), ('port', '3306'), ('database', 'TestDB')]



# 7、往配置文件中增加章节section

# 重新实例化一个对象，如果使用上面已经read的对象的话，write的时候会将已经读的内容再写一遍。
writeConfig = ConfigParser.ConfigParser()

# 8、增加章节section
writeConfig.add_section("UserInfo")

# 9、set 往配置文件中的[UserInfo]节点加入键值对

writeConfig.set("UserInfo",'username','TestYang')

writeConfig.set("UserInfo",'password','TestYangPassWord')

writeConfig.set("UserInfo",'age','18')

writeConfig.set("UserInfo",'country','China')

# 10、已追加的方式打开已经存在的文件，如果文件不存在则创建该文件

# writeConfig.write(open('testconfig.ini','a'))

# 上面的写入代码等价于下面的代码
'''
f = open('testconfig.ini','a')
writeConfig.write(f)
'''

# 注意 如果 分开先写  writeConfig.add_section("UserInfo") 然后在单独执行set 会报如下错误
# 所以 add_section 和 set 要一起写，一起执行
'''
  raise NoSectionError(section)
ConfigParser.NoSectionError: No section: 'UserInfo'
'''
# 写入后的结果如下
'''
[UserInfo]
username = TestYang
password = TestYangPassWord
age = 18
country = China
'''


# 11、按照类型读取指定section 的option 信息 有getint 同样的还有getfloat、getboolean。

# 返回为string类型
print config.get("UserInfo",'age')
# 返回为int类型
print config.getint("UserInfo",'age')

# 12、移除option

config.remove_option('UserInfo','age')

# 13、 移除section， 移除节点后，节点下的键值对一起移除
config.remove_section('UserInfo')

# 只要有修改就要写回文件保存
config.write(open("testconfig.ini", "w"))

# 其他格式的配置文件
# cf.write(open("test.conf", "w"))

# 应用实例，可以新建一个py文件，将使用的方法封装起来

class ReadConfig():
    def __init__(self):

        self.cf = ConfigParser.ConfigParser()
        self.cf.read(configFile)

    def get_UserInfo(self, username):
        value = self.cf.get("UserInfo", username)
        return value



    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value


if __name__ == "__main__":
    getdata = ReadConfig()
    print  getdata.get_UserInfo("username") # TestYang
    print  getdata.get_db("database")  # TestDB








