#coding=utf-8、
# pip3 install xlrd,xlwt
import xlrd,xlwt

#打开Excel文件读取数据
data = xlrd.open_workbook('../resource/income_tax.xls')


#获取一个工作表

#通过索引顺序获取
table = data.sheets()[0]

#通过索引顺序获取
table2 = data.sheet_by_index(0)

#通过名称获取
table3 = data.sheet_by_name(u'Sheet1')

# 修改单元格 #垃圾xlwt好像不能修改单元格值
# ctype 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
table.put_cell(0, 0, 1, "米", 0)

for i in range(table.nrows):
    for j in  range(table.ncols):
        cell = table.cell(i,j)
        print(cell.value)


workBook = xlwt.Workbook()
sheet = workBook.add_sheet("工作表1")
sheet.write(0,1,"ganjuehaolihai")
workBook.save("../resource/test.xls")


