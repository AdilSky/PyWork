#-*-coding:utf-8-*-
# Time:2017/10/11 23:17
# Author:YangYangJun

#学习 python  函数中参数的使用。

# 以下是调用函数时可使用的正式参数类型：
#
# 必备参数  -- 位置参数
#
# 默认参数
#
# 关键字参数
#
# 可变参数
#
# 关键字可变参数

# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。


# 必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
# 调用函数，你必须传入一个参数，不然会出现语法错误：

def mustParams(param1,param2):

    print "mustParam1:", param1

    print "mustParam2:", param2
    # 执行结果 参见调用方法
    # mustParam1: 12
    # mustParam2: 23

# 调用函数时，默认参数的值如果没有传入，则被认为是默认值

def defaultParams(param1,param2= '你好'):

    print "defaultParam1:", param1

    print "defaultParam2:", param2
    print  param1,param2

    # 执行结果 参见调用方法
    # defaultParam1: 小明
    # defaultParam2: 你好
    # 小明 你好
    # defaultParam1: 小明
    # defaultParam2: 干活
    # 小明 干活

# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

def keywordParams(param1,param2):

    print "keywordParam1:", param1

    print "keywordParam2:", param2

    #执行结果 参见调用方法
    # keywordParam1: 518
    # keywordParam2: 988
    # keywordParam1: 988
    # keywordParam2: 518
    # keywordParam1: 988
    # keywordParam2: 518


# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做可变参数,python会将这些多出来的参数放入一个元组中
# 在实际的使用中，我们经常会同时用到必选参数、默认参数、可变参数和关键字参数或其中的某些。但是，需要注意的是，
# 它们在使用的时候是有顺序的，依次是必选参数、默认参数、可变参数和关键字可变参数。
# 注意 可变参数和关键字可变参数 不能和关键字参数一起使用
def variableParams(param1,param2,param3=56,*args):

    print "variableParam1:", param1

    print "variableParam2:", param2
    print "variableParam3:", param3
    print "variableParamargs:", args

    #执行结果
    # variableParam1: 12
    # variableParam2: 25
    # variableParam3: 568
    # variableParamargs: (456, 125)


# “关键字”“可变长”顾名思义是允许在调用时传入多个“关键字”参数，python会将这些多出来的<参数名, 参数值>放入一个字典中。需要注意的是，关键字变量参数应该为函数定义的最后一个参数，带**

def variableKeywordParames(**kwargs):

    print "variableKeywordParames:",kwargs
    # 执行结果
    # variableKeywordParames: {'age': 18, 'param2': 58, 'param1': 12, 'name': 'Tester'}


# 当非关键字可变长参数和关键字可变长参数出现在同一个函数中时，他们应当遵守如下的顺序约定：

def newfoo(normal1, normal2,normal3='testParam', *args, **kw):
    print "normal1:",normal1
    print "normal2:",normal2
    print "normal3:",normal3
    print "args:",args
    print "kw:",kw

    #执行结果 参见调用方法
    # normal1: 1
    # normal2: 2
    # normal3: 3
    # args: (4, 5, 6)
    # kw: {'age': 18, 'name': 'Tester'}


if __name__ == '__main__':

    #必备参数调用
    mustParams(12,23)

    #默认参数调用
    defaultParams("小明")
    defaultParams("小明","干活")

    #关键字参数调用
    keywordParams(param2=988,param1=518)
    keywordParams(param1=988,param2=518)
    #注释代码是会出错的代码即，这种写法不可用
    #keywordParams(param1=988,518)
    #keywordParams(param2=988,518)
    # keywordParams(988, param1=518)
    #TypeError: keywordParams() got multiple values for keyword argument 'param1'
    keywordParams(988, param2=518)
    #由此可见如果关键字参数与必选参数再起的使用时，关机字参数要在必选参数之后，且参数名要与定义函数时参数顺序一致
    #如果参数全为关键字参数，则可以忽略先后顺序

    # 可变参数调用，注意不能添加关键字参数
    variableParams(12,25,568,456,125)

    variableKeywordParames(param1 = 12,param2 = 58,name = "Tester",age = 18)

    newfoo(1,2,3,4,5,6,name = "Tester",age = 18)
