# coding: utf-8
#

import time,openpyxl
fileName = 'C:/Users/Administrator/Desktop/74年及之前出生未补缴农保名单_20191202.xlsx'

book = openpyxl.load_workbook(fileName)
sheet = book['sheet']

for rowNum in range(2,sheet.max_row+1):
    retireYear = sheet.cell(rowNum, 10) #到龄日期
    paidMonth = sheet.cell(rowNum, 13) #累计已缴费月数
    finishPayYear = sheet.cell(rowNum, 20) #预计缴清年份
    canPayoffBeforeRetire = sheet.cell(rowNum, 21) #是否60之前缴清
    startPayYear = sheet.cell(rowNum, 21)
    # print(retireYear.value, paidMonth.value, finishPayYear.value, canPayoffBeforeRetire.value)
    # print(type(retireYear.value), type(paidYearNum.value))

    x = int(paidMonth.value)//12
    y = int(retireYear.value[:4])
    print(x,y,x+y)
    needPayYear = y - 2010
    if needPayYear > 15: needPayYear = 15
    finishPayYear.value = 2019 + needPayYear -x
    if x+y >= 2034:
        canPayoffBeforeRetire.value = '是'
    else:
        canPayoffBeforeRetire.value = '否'

book.save(fileName)