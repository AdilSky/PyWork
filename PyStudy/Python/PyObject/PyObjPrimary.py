#-*-coding:utf-8-*-
# Time:2017/10/19 20:21
# Author:YangYangJun

# python 面向对象初级学习阶段

# 今天我们来学习一种新的编程方式：面向对象编程（Object Oriented Programming，OOP，面向对象程序设计）
# 注：Java和C#来说只支持面向对象编程，而python比较灵活即支持面向对象编程也支持函数式编程
#

#创建一个类

# class EmployeeInfo():
#     '创建一个员工信息类'   # 类文档字符串 位置在类名下单引号中， 类的帮助信息可以通过ClassName.__doc__查看。
#
#     #class_suite   类体  由类成员，方法，数据属性组成。
#
# print EmployeeInfo.__doc__   # 创建一个员工信息类
#


# 创建一个类，应用实例

class EmployeeInfo():
    '员工信息类'

    # 定义员工数量，初始化为0 ，每实例化一个对象时，数量增 1
    empCount = 0

    def __init__(self,name,age):  # 类中的函数第一个参数必须是self（详细见：类的三大特性之封装）类中定义的函数叫做 “方法”

        self.name = name
        self.age = age
        # EmployeeInfo.empCount += 1
        EmployeeInfo.empCount += 1

    def displayEmployeeInfo(self):

        print "员工姓名：",self.name,"员工年龄：",self.age,"员工序号：",EmployeeInfo.empCount


emp1 = EmployeeInfo("Tester",18)

emp1.displayEmployeeInfo()  # 输出结果 员工姓名： Tester 员工年龄： 18 员工序号： 1

emp2 = EmployeeInfo("Manager",19)

emp2.displayEmployeeInfo()  # 员工姓名： Manager 员工年龄： 19 员工序号： 2

# 创建一个测试类

class Test:
    '创建一个测试类'
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()

# 如果存在 'age' 属性返回 True。
print hasattr(emp1,'age') # True
# 返回 'age' 属性的值
print getattr(emp1,'age') # 18
# 添加属性 'num' 值为 1
print setattr(emp1,'num',1) # None
# 返回 'num' 属性的值
print getattr(emp1,'num') # 1
# 删除属性 'age'
print delattr(emp1,'num') # None



print "EmployeeInfo.__doc__:", EmployeeInfo.__doc__
print "EmployeeInfo.__name__:", EmployeeInfo.__name__
print "EmployeeInfo.__module__:", EmployeeInfo.__module__
print "EmployeeInfo.__bases__:", EmployeeInfo.__bases__
print "EmployeeInfo.__dict__:", EmployeeInfo.__dict__


class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr


class Child(Parent):  # 定义子类
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print '调用子类方法'

p = Parent

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值

print issubclass(Child,Parent) #  True  issubclass() - 布尔函数判断第一个类是第二个类的子类或者子孙类，语法：issubclass(子类名,父类名)

print isinstance(c,Parent) # True  isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。








