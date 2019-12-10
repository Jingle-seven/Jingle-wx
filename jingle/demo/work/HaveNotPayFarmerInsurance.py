# coding: utf-8
# 未缴农保名单，txt转excel，删掉0

import openpyxl
from openpyxl.styles import Border, Side

country = '云西未缴农保_20191129'
dir = 'C:/Users/Administrator/Desktop/农保未续缴明细/'
txtPath = dir + country +'.txt'
txtFile = open(txtPath,encoding='gbk')

wbook = openpyxl.Workbook()
sheet = wbook['Sheet'] # 使用默认的Sheet
tableHead = ['序号', '姓名', '身份证', '档次', '账号', '已交月份']
sheet.append(tableHead)
# 数据
rowNum = 2
for line in txtFile:
    what = line.split('|')
    # print(type(what),what)
    if line.startswith('#'): continue
    if what[13] == '0': continue #删掉已交0期的数据
    sheet.cell(rowNum, 1).value = rowNum - 1
    sheet.cell(rowNum, 2).value = what[2]
    sheet.cell(rowNum, 3).value = what[3]
    sheet.cell(rowNum, 4).value = what[6]
    sheet.cell(rowNum, 5).value = what[10]
    sheet.cell(rowNum, 6).value = what[13]
    rowNum  = rowNum + 1

# 边框
thin = Side(border_style="thin", color="000000")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
for row in sheet['A1:F%s'%(rowNum-1)]:
    for cell in row:
        cell.border = border
# 列宽
sheet.column_dimensions['A'].width = 4
sheet.column_dimensions['B'].width = 8
sheet.column_dimensions['C'].width = 20
sheet.column_dimensions['D'].width = 22
sheet.column_dimensions['E'].width = 20
sheet.column_dimensions['F'].width = 8


print('%s end'%(rowNum-2))
wbook.save(dir + country +'.xlsx')