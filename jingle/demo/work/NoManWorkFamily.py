# coding: utf-8
# 每月农保待遇核定名单，用来通知到龄人员来开始领取待遇，txt转excel，删掉无效人名

import openpyxl
import jingle.demo.work.SkData as SkData

xlsName = '贫困户名单20200222'
dir = 'C:/Users/Administrator/Desktop/其他/'

rawBook = openpyxl.load_workbook(dir + xlsName + '.xlsx')
resBook = openpyxl.Workbook()
sheet1 = resBook.worksheets[0]# 使用默认的Sheet
sheet1.title = '零就业' # 更改表名

nameToFamily = dict()
for row in rawBook.worksheets[0].values:
    name = row[5]
    if name in nameToFamily:
        nameToFamily[name].append(row)
    else:
        nameToFamily[name] = [row]
    # print(row)
    # print(row[5],row[32],row[51])
    # sheet1.append(row)
    if row[32]=='普通劳动力' and row[51]=='':
        print(row[5],row[32],row[51])
print(nameToFamily)

for k,v in nameToFamily.items(): #每一户家庭
    hasLabor = False # 家庭是否有至少一个劳动力
    hasWork = False # 家庭是否至少有一个成员有工作
    for row in v: # 每一个家庭成员
        if row[32] == '普通劳动力':
            hasLabor = True
        if row[51] != '':
            hasWork = True
            break
    if hasLabor and not hasWork: #如果家庭有劳动力但是所有人都没工作
        for row in v: sheet1.append(row)
    if k=='户主姓名': #表头
        for row in v: sheet1.append(row)
resBook.save(dir + xlsName + '零就业.xlsx')
print("end")
