# coding=utf-8
# pip3 install xlrd,xlwt
import xlrd,xlwt

#打开Excel文件
data = xlrd.open_workbook('../resource/income_tax.xls')

#获取一个工作表
#通过索引顺序获取
table = data.sheets()[0]
#通过索引顺序获取
table2 = data.sheet_by_index(0)
#通过名称获取
table3 = data.sheet_by_name(u'Sheet1')

# 修改单元格
# #垃圾xlwt好像不能修改单元格值，在pypi找不到put_cell方法的文档，
# Stack Overflow找了一会也没看到put_cell的正确用法，大多是推荐使用xlutils和openpyxl
# xlutils基于xlrd,xlwt，估计也是垃圾得半斤八两，那么就用openpyxl
# 方法第三个参数 ctype 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
table.put_cell(0, 0, 1, "米", 0)

# 读取
for i in range(table.nrows):
    for j in  range(table.ncols):
        cell = table.cell(i,j)
        print(cell.value)

#创建
workBook = xlwt.Workbook()
sheet = workBook.add_sheet("工作表1")
sheet.write(0,1,"不要停下来啊！")
workBook.save("../resource/test.xls")


