#-*-coding:utf-8-*-
# Time:2017/9/21 19:02
# Author:YangYangJun


from openpyxl import Workbook


import os
import time



def writeExcel():
    # 获取文件路径
    excelPath = os.getcwd()
    print "****"
    print excelPath

    # 定义文件名称
    #  invalid mode ('wb') or filename: 'Excel2017-09-21_20:15:57.xlsx'   这种方式明明文件，会提示保存失败，无效的文件名。
    # nameTime = time.strftime('%Y-%m-%d_%H:%M:%S')
    nameTime = time.strftime('%Y-%m-%d_%H-%M-%S')
    excelName = excelPath + 'Excel' + nameTime + '.xlsx'
    print excelName

    wb = Workbook()

    ws = wb.active

    tableTitle = ['userName', 'Phone', 'age', 'Remark']

    # 维护表头
    #        if row < 1 or column < 1:
    #          raise ValueError("Row or column values must be at least 1")
    # 如上，openpyxl 的首行、首列 是 （1,1）而不是（0,0），如果坐标输入含有小于1的值，提示 ：Row or column values must be at least 1，即最小值为1.
    for col in range(len(tableTitle)):
        c = col + 1
        ws.cell(row=1, column=c).value = tableTitle[col]

    # 数据表基本信息
    tableValues = [['杨要军', 15201062199, 18, '测试数据！'], ['李雷', 15201062198, 19, '测试数据！'],
                   ['Marry', 15201062191, 28, '测试数据！']]

    for row in range(len(tableValues)):
        ws.append(tableValues[row])

    wb.save(filename=excelName)







if __name__ == '__main__':
    excelPath = os.getcwd()
    print "****"
    print excelPath
    writeExcel()




