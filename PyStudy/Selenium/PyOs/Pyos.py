#-*-coding:utf-8-*-
# Time:2017/9/27 14:02
# Author:YangYangJun

import os

#返回当前工作目录
currentpath = os.getcwd()

print  os.listdir(currentpath)  # ['newFile', 'Pyos.py']

print currentpath  # D:\WorkSpace\Python\Study\Selenium\PyOs
#拼接目录或文件路径
newpath = os.path.join(currentpath,'newFile')

fileNamePath = os.path.join(currentpath,'newFile.xls')
print fileNamePath   # D:\WorkSpace\Python\Study\Selenium\PyOs\newFile.xls

print newpath   # D:\WorkSpace\Python\Study\Selenium\PyOs\newFile

print os.access(newpath,os.X_OK)

# os.chdir(path)  改变当前工作目录
print os.chdir(newpath)  #这个返回值为空 None

print os.getcwd()  # D:\WorkSpace\Python\Study\Selenium\PyOs\newFile

print __file__  # D:/WorkSpace/Python/Study/Selenium/PyOs/Pyos.py

print __name__  # __main__

#print chnewpath


print os.listdir(currentpath)  # ['newFile', 'Pyos.py']

#返回path指定的文件夹包含的文件或文件夹的名字的列表。

# 在当前目录下创建新的目录注意是创建目录而不是文件
#os.mkdir("testFile")

#os.mkdir("testFile.xls")


#注意删除的是文件而不是路径
#删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
#os.remove('123')

#os.removedirs("testFile") #删除该目录

#os.rename('testFile','fileTest')

#os.rename() 方法用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError。
#os.rename(src, dst)
#src -- 要修改的目录名
#dst -- 修改后的目录名

#os.renames() 方法用于递归重命名目录或文件。类似rename()。
#os.renames(old, new)
#old -- 要重命名的目录
#new --文件或目录的新名字。甚至可以是包含在目录中的文件，或者完整的目录树。

print "当前目录为: %s" %os.getcwd()

# 列出目录
print "目录为: %s"%os.listdir(os.getcwd())

# 重命名 "fileTest"
os.renames("fileTest","fileTest1/fileTest2")

print "重命名成功。"

# 列出重命名的文件 "fileTest1"
print "目录为: %s" %os.listdir(os.getcwd())


#os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。
#os.rmdir(path)
#path -- 要删除的目录路径
#该方法没有返回值
