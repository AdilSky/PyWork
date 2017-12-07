#-*-coding:utf-8-*-
# Time:2017/9/20 20:13
# Author:YangYangJun

import xlrd,xlwt,xlutils
import os
import time
#导入copy 方法方便文件写操作。
from xlutils.copy import copy

'''
导入 excel操作的三个模块
xlrd  读取操作
xlwt  写入操作
xlutils 复制、剪切、粘贴等操作

'''

#获取当前文件路径
# currntPath = os.getcwd()
# print currntPath
# #D:\WorkSpace\Python\Study\Selenium\PyExcel
#
# #获取excel文件路径
# excelPath = os.path.join(os.getcwd(),'ExcelData')
# print excelPath
# #D:\WorkSpace\Python\Study\Selenium\PyExcel\ExcelData
#
# #遍历获取文件名
# excelPathDir = os.listdir(excelPath)
# print excelPathDir
# #['PyExcel.xlsx']
# #excel与程序在同一目录下，可以直接数据文件名。
#
# #excelName = 'PyExcel.xlsx'
#
# #如果不在一个目录下，最好填写绝对路径
#
# #excelName = os.path.join(excelPath,'PyExcel.xlsx')
# excelName = os.path.join(excelPath,excelPathDir.pop())
# print  excelName
# #D:\WorkSpace\Python\Study\Selenium\PyExcel\ExcelData\PyExcel.xlsx
#
# ReadExcel = xlrd.open_workbook(excelName)
#
# print ReadExcel.sheet_names()
# # 返回的是sheet页list [u'userInfo', u'tests']


def OpenXlxs():

    xlsxPath = os.path.join(os.getcwd(),'ExcelData')
    xlsxPathDir = os.listdir(xlsxPath)
    xlsxName = os.path.join(xlsxPath,xlsxPathDir.pop())
    print xlsxName
    readOpenXlsx = xlrd.open_workbook(xlsxName)

    readXlsxSheet = readOpenXlsx.sheet_by_name('userInfo')
    # copy管道作用
    writeOpenXlsx = copy(readOpenXlsx)

    print readXlsxSheet,writeOpenXlsx,xlsxName
    return readXlsxSheet,writeOpenXlsx,xlsxName

def readXlsx(readXlsxSheet, writeOpenXlsx, xlsxName):
    #获取行数
    print "***"
    rowMax = readXlsxSheet.nrows
    print rowMax # 4
    #获取第一行的值
    rows = readXlsxSheet.row_values(0)
    print rows

    #获取列数
    colMax = readXlsxSheet.ncols
    print colMax   # 8

    for r in range(rowMax):
        if r == 0:
            continue
        else:
            rows = readXlsxSheet.row_values(r)
            print rows
            RunValue = readXlsxSheet.cell(r,6).value
            if RunValue == 'Y':
                writeXlsx(writeOpenXlsx,r,xlsxName)


def writeXlsx(writeOpenXlsx,row,xlsxName):
    # 前面已经通过 copy 方法获取了writeOpenXlsx
    # 通过get_sheet()获取的sheet有write()方法
    writeXlsxSheet = writeOpenXlsx.get_sheet(0)
    modifyTime = time.strftime('%Y-%m-%d')
    print modifyTime
    writeXlsxSheet.write(row,4,modifyTime)
    writeXlsxSheet.write(row,7,'Pass')
    writeOpenXlsx.save(xlsxName)


if __name__ == '__main__':
    readXlsxSheet, writeOpenXlsx, xlsxName = OpenXlxs()

    readXlsx(readXlsxSheet, writeOpenXlsx, xlsxName)

