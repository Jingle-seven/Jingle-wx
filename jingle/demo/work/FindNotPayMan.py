# coding: utf-8
# 从总参保人中减去本年已交的人员，得出本年未交农保的人员名单

import openpyxl,os,time
import jingle.demo.work.SkData as SkData


# xlsName = '12月已缴农保_20191223'
# txtPath = dir + xlsName + '.txt'
allManTxt = 'C:/Users/Administrator/Desktop/农保未续缴明细/水口镇农保60岁以下人员_20200811.txt'
HavePaidManDir = 'C:/Users/Administrator/Desktop/农保未续缴明细/已缴农保/'
statisticsFileName = HavePaidManDir + '已缴人员汇总统计表2020.xlsx'
strTime = time.strftime("%Y%m%d", time.localtime())

def readManAsDict(txtFilePath):
    allManCount = 0
    poorManCount = 0
    idToRow = dict()
    txtFile = open(txtFilePath)
    for line in txtFile:
        # print(line)
        if '#' in line: continue
        r = line.split('|')
        allManCount = allManCount +1
        if r[17].find('特殊人群0元缴费档次') >= 0 :
            poorManCount = poorManCount +1
            continue
        idToRow[r[6]] = r
    print('共{}人，其中普通账户{}人，特殊参保户{}人'.format(allManCount,allManCount-poorManCount,poorManCount))
    return idToRow

# 文件路径，写入的列
def analyseOneFile(txtPath,idToRow):
    txtFile = open(txtPath,'rb') #因为有乱码，用正常文本解析会报错，只能用二进制解析
    for line in txtFile:
        # print(line)
        if '#' in str(line[:10], encoding="gbk"): continue
        row = line.split(b'|')
        # print(str(recordArr[12], encoding="gbk"))
        if '期缴' == str(row[12], encoding="gbk"):
            id = str(row[3], encoding="gbk")
            # print(id)
            if id in idToRow:
                idToRow.pop(id)

def writeExcel(restMan,idToHouseholdInfo):
    destDir = 'C:/Users/Administrator/Desktop/农保未续缴明细/未交农保'+ strTime
    if not os.path.exists(destDir):
        os.mkdir(destDir)
    # 初始化文件
    tableHead = ['序号', '村委会', '姓名', '身份证号', '档次（今年未交农保）',  '已交月数', '村小组']
    for v in SkData.villages:
        v.book = openpyxl.Workbook()
        v.book.worksheets[0].append(tableHead)
    # 分村
    for k,r in restMan.items():
        if not r[3].isdecimal():
            continue
        v = SkData.idToVillage[r[3]]
        v.count = v.count + 1
        houseHoldInfo = ['','','','',]
        # print(r[5])
        if r[6] in idToHouseholdInfo:
            houseHoldInfo = idToHouseholdInfo[r[6]]
        v.book.worksheets[0].append([v.count, v.name, r[5], r[6], r[17], r[15],houseHoldInfo[1]])
    #保存
    for v in SkData.villages:
        SkData.setBorderWidth(v.book.worksheets[0], 25) # 设置边框直到25行
        v.book.save(destDir +'/'+v.name+'历年和本年未交农保'+strTime+'.xlsx')
    print('保存到 %s'%destDir)

def readHouseholdInfo():
    idToHouseholdInfo = dict()
    book = openpyxl.load_workbook('C:/Users/Administrator/Desktop/水口公共服务/部门数据.xlsx')
    lastMaster = ''
    lastHouseholdCode = ''
    for row in book.worksheets[0].values:
        # print(row[0], row[2], row[6], row[21], )
        # 身份证号，村小组，户号，户主姓名
        info = [row[6],row[0],row[2],'']
        if row[21]=='户主':
            lastMaster = row[3]
            lastHouseholdCode = row[2]

        if row[2] == lastHouseholdCode:
            info[3] = lastMaster
        idToHouseholdInfo[info[0]] = info
    return idToHouseholdInfo
if __name__ == '__main__':
    # 读取所有人
    allManIdToRow = readManAsDict(allManTxt)
    # 去掉已交的人
    for oneTxtFile in os.listdir(HavePaidManDir):# 每月一个文件，oneTxtFile的文件名例子：06月已缴农保_20191223.txt
        if oneTxtFile[-3:]== 'txt': # 如果是文本文件才解析
            # 根据月份设置写入的行
            filePath = HavePaidManDir + '/' + oneTxtFile
            analyseOneFile(filePath,allManIdToRow)
    print('%s人未交农保'%len(allManIdToRow))
    # 分村写入文件
    idToHouseholdInfo = readHouseholdInfo()
    writeExcel(allManIdToRow,idToHouseholdInfo)
    # xsl.save(statisticsFileName)