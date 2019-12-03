# coding: utf-8
# 未缴农保名单，txt转excel，删掉0

import time,openpyxl
country = '云西未缴农保_20191129'
dir = 'C:/Users/Administrator/Desktop/农保未续缴明细/'
txtPath = dir + country +'.txt'
txtFile = open(txtPath,encoding='gbk')

wbook = openpyxl.Workbook()
sheet = wbook.create_sheet('sheet1') #TODO 使用默认的sheet而不是新建
tableHead = ['序号', '姓名', '身份证', '档次', '账号', '已交月份']
for i in tableHead:
    sheet.cell(1, tableHead.index(i) + 1).value = i #表头

rowNum = 2
for line in txtFile:
    what = line.split('|')
    print(type(what),what)
    if line.startswith('#'): continue
    if what[13] == '0': continue #删掉已交0期的数据
    sheet.cell(rowNum, 1).value = rowNum - 1
    sheet.cell(rowNum, 2).value = what[2]
    sheet.cell(rowNum, 3).value = what[3]
    sheet.cell(rowNum, 4).value = what[6]
    sheet.cell(rowNum, 5).value = what[10]
    sheet.cell(rowNum, 6).value = what[13]
    rowNum  = rowNum + 1

wbook.save(dir + country +'.xlsx')