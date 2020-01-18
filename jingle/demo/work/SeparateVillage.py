# coding: utf-8
# 把各种excel分村委，按村委分成多个sheet
# TODO 未完成

import openpyxl,time
import jingle.demo.work.Data as Data

startTs = time.time()
colHead = ['序号', '公安户籍编号', '姓名', '公民身份号码', '户籍地址', '未参保原因']
nameToColProp = {
    '序号':Data.ColProp('序号',2,remark=-1),
    '公安户籍编号':Data.ColProp('公安户籍编号',6,remark=-1),
    '姓名':Data.ColProp('姓名',4,remark=-1),
    '公民身份号码':Data.ColProp('公民身份号码',18,remark=-1),
    '户籍地址':Data.ColProp('户籍地址',20,remark=-1),
    '未参保原因':Data.ColProp('未参保原因',5,remark=-1),
}
xlsName = '南雄市2019参保2020未参保名单'
dir = 'C:/Users/Administrator/Desktop/'

rawBook = openpyxl.load_workbook(dir + xlsName + '.xlsx')
resBook = openpyxl.Workbook()
resBook.remove(resBook.worksheets[0])
skColHead = '街镇'
skColValue = '水口镇'
separateColHead = '社区村'
skColHeadIdx = 0
separateColHeadIdx = 0

nameToVillage = {}
for v in Data.villages: #创建工作表，并保存工作表的引用。写备注,创字典，便于后面匹配
    v.obj = resBook.create_sheet(v.name)
    v.obj.append(colHead) #表头
    if v.name == '社区':
        v.remark = '水口社区居委会'
    else:
        v.remark = v.name + '村委会'
    nameToVillage[v.remark] = v

print(rawBook.sheetnames)
s1 = rawBook.worksheets[0]
s2 = rawBook.worksheets[1]
nowSheet = s1
counter = 1
# for i in range(1,nowSheet.max_row):
#     row = nowSheet[i] # 用下标取值效率过低，耗时是values方法的十倍，可能是因为要构造大量cell对象
    # rowValue = [cell.value for cell in s1[i]] # s2[i]是一行元素为Cell的元组，转换为value的list更直接，便于使用
for row in nowSheet.values:
    if counter==1:# 找出水口镇过滤条件的那一列的序号，存入skTbHeadIdx.分类条件，存入separateColHeadIdx
        skColHeadIdx = row.index(skColHead)
        separateColHeadIdx = row.index(separateColHead)
        for k,v in nameToColProp.items():
            # print(k,v)
            try:
                v.remark = row.index(k)
            except Exception as e:
                print(k,e)
                pass
        #
    if row[skColHeadIdx] == skColValue: #如果是水口镇，将数据写入到对应村委工作表
        village = nameToVillage[row[11]]
        village.count +=1
        resRow = [village.count]
        for k,v in nameToColProp.items():
            if v.remark!=-1:
                resRow.append(row[v.remark])
        village.obj.append(resRow)
    counter += 1
    # print(row)
print('处理了{}行数据，耗时{:.2f}秒'.format(counter,time.time() - startTs))
resBook.save(dir + xlsName + '-水口分村委.xlsx')