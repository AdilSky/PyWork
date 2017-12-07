#-*-coding:utf-8-*-
# Time:2017/9/20 20:13
# Author:YangYangJun

import xlrd,xlwt,xlutils
import os

'''
导入 excel操作的三个模块
xlrd  读取操作
xlwt  写入操作
xlutils 复制、剪切、粘贴等操作

'''

#获取当前文件路径
currntPath = os.getcwd()
print currntPath
#D:\WorkSpace\Python\Study\Selenium\PyExcel

#获取excel文件路径
excelPath = os.path.join(os.getcwd(),'ExcelData')
print excelPath
#D:\WorkSpace\Python\Study\Selenium\PyExcel\ExcelData

#遍历获取文件名
excelPathDir = os.listdir(excelPath)
print excelPathDir
#['PyExcel.xlsx']
#excel与程序在同一目录下，可以直接数据文件名。

#excelName = 'PyExcel.xlsx'

#如果不在一个目录下，最好填写绝对路径

#excelName = os.path.join(excelPath,'PyExcel.xlsx')
excelName = os.path.join(excelPath,excelPathDir.pop())
print  excelName
#D:\WorkSpace\Python\Study\Selenium\PyExcel\ExcelData\PyExcel.xlsx



ReadExcel = xlrd.open_workbook(excelName)

print ReadExcel.sheet_names()
# 返回的是sheet页list [u'userInfo', u'tests']


def readOpenXlxs():

    xlsxPath = os.path.join(os.getcwd(),'ExcelData')
    xlsxPathDir = os.listdir(xlsxPath)
    xlsxName = os.path.join(xlsxPath,xlsxPathDir.pop())
    print xlsxName
    openXlsx = xlrd.open_workbook(xlsxName)

    xlsxSheet = openXlsx.sheet_by_name('userInfo')
    print xlsxSheet
    return xlsxSheet


def writeOpenXlxs():
    xlsxPath = os.path.join(os.getcwd(), 'ExcelData')
    xlsxPathDir = os.listdir(xlsxPath)
    xlsxName = os.path.join(xlsxPath, xlsxPathDir.pop())
    print xlsxName
    openXlsx = xlwt.open_workbook(xlsxName)

    xlsxSheet = openXlsx.sheet_by_name('userInfo')
    print xlsxSheet
    return xlsxSheet


def readXlsx(xlsxSheet):
    #获取行数
    #rowNums =  xlsxSheet.row_len()
    rowMax = xlsxSheet.nrows
    #print rowNums
    print rowMax
    rows = xlsxSheet.row_values(0)
    print rows  # 4

    #获取列数
    colMax = xlsxSheet.ncols
    print colMax   # 8

    for r in range(rowMax):
        i = r+1
        RunValue = xlsxSheet.cell(i,6).value
        if RunValue == 'Y':
            writeXlsx(i,6)


def writeXlsx(xlsxSheet):
    rowMax = xlsxSheet.nrows
    # print rowNums
    print rowMax
    rows = xlsxSheet.row_values(0)
    print rows  # 4

    # 获取列数
    colMax = xlsxSheet.ncols
    print colMax  # 8

    for r in range(rowMax):
        i = r + 1
        RunValue = xlsxSheet.cell(i, 6).value
        if RunValue == 'Y':
            writeXlsx(i, 6)







if __name__ == '__main__':
    readXlsxSheet = readOpenXlxs()
    readXlsx(readXlsxSheet)
    writeXlsxSheet = writeOpenXlxs()
    writeXlsx(writeXlsxSheet)

    pass





























