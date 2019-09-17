# coding utf-8
# 选取几个指数, 计算它们年线与当天数值的差距, 将所有差距加和乘以3再加一百, 作为总金额投资系数,即将差距放大三倍
# 总金额投资系数乘以原投资金额,作为计划投资金额
# 以最低的差距作为0, 其他差距减去最低差距作为权重, 算出所有指数占总投资金额的百分比
# 将百分比乘以计划投资金额, 得出各指数投入金额
# import xlrd,xlwt
import time,openpyxl,tushare

# 指数类，包含指数当前点数和最终投资金额等信息
class IndexToMa250:
    def __init__(self, name, index, MA250, code=""):
        self.name = name #指数名
        self.index = index #指数点数
        self.MA250 = MA250 #指数年线
        self.investmentFactor = self.MA250*100/self.index - 100 #指数与年线的差
        self.advanceFactor = 0 #（此指数与年线偏离程度）减去（最low的指数与年线偏离程度），作为投资金额中占比因子
        self.advancePercentage = 0 #在投资金额中的占比
        self.finalMoney = 0 #最终投资金额
        self.code = code #投资的基金代码

# 计算最终投资金额
def calculateFinalMoney(someIndexes):
    lowestIdx = someIndexes[0] #最low的指数
    totalInvestmentFactor = 0 #第一投资系数,用于计算总投资
    totalAdvanceFactor = 0 #第二投资系数,用于计算各指数投资占比
    for i in someIndexes: #加和第一投资系数(用于计算总投资金额),并找出最小的投资系数
        totalInvestmentFactor = totalInvestmentFactor + i.investmentFactor
        if i.investmentFactor < lowestIdx.investmentFactor:
            lowestIdx = i

    print("最小系数:\t\t %.2f %s" % (lowestIdx.investmentFactor,lowestIdx.name))
    #汇总所有指数减去最小投资系数后的值(即计划投资系数),得到总计划投资系数.
    # 也就是说,最小的那个指数, 投资0元. 以此指数为基础,偏离越大投资占比越大
    for i in someIndexes:
        i.advanceFactor = i.investmentFactor - lowestIdx.investmentFactor
        totalAdvanceFactor = totalAdvanceFactor + i.advanceFactor
    for i in someIndexes: #每个指数计划投资系数除以第二系数,得到每个指数占总投资金额的百分比
        i.advancePercentage = i.advanceFactor / totalAdvanceFactor

    print("总定投系数:\t\t %.2f"%(totalInvestmentFactor + 100))
    # 系数放大三倍,也就是以当天所有指数平均值为基准,如果年线在平均值66%则停止定投,年线在133%时加倍定投,166%时3倍定投
    planMoney = rawMoney * (totalInvestmentFactor*3 +100) /100

    print("计划定投金额:\t %.2f (总定投系数扩大三倍)"%planMoney)
    # print("总定投系数", divideByFactor)
    for i in someIndexes:
        i.finalMoney = i.advancePercentage * planMoney
        print("%s:\t %.2f"% (i.name,i.finalMoney))

def writeExcel(sIdxes):
    excelPath = '../resource/定投记录.xlsx'
    nowDateStr = time.strftime("%Y-%m-%d", time.localtime())
    nowYearStr = time.strftime("%Y", time.localtime())
    totalMoney = 0
    detailSheetRowNames = ["指数名","指数值","年线","偏离程度","投资因子","投资金额"]
    summarySheetRowNames = ["日期","总金额"]#汇总表的各列名
    for i in sIdxes:
        summarySheetRowNames.append(i.name)
        totalMoney = totalMoney + i.finalMoney
    try: wbook = openpyxl.load_workbook(excelPath)
    except FileNotFoundError as e: #文件不存在就创建新文件
        wbook = openpyxl.Workbook()
        sSheet = wbook.create_sheet(nowYearStr) # 汇总表summarySheet
        for i in summarySheetRowNames: sSheet.cell(1,summarySheetRowNames.index(i)+1).value = i #汇总表表头
        wbook.save(excelPath)
    sSheet = wbook[nowYearStr]
    #如果汇总表的最后一行的日期是今天，那么覆盖其数据，因为一天最多一次
    if sSheet.cell(sSheet.max_row,1).value == nowDateStr:
        nowSSheetRow = sSheet.max_row
    else:
        nowSSheetRow = sSheet.max_row + 1
    sSheet.cell(nowSSheetRow,1).value = nowDateStr #填写汇总表数据,日期和总金额
    sSheet.cell(nowSSheetRow,2).value = round(totalMoney,1)
    try: dSheet = wbook[nowDateStr] #明细表detailSheet,存在的话就修改，不存在就新建一个
    except KeyError as e:
        dSheet = wbook.create_sheet(nowDateStr)
    for i in detailSheetRowNames: dSheet.cell(1,detailSheetRowNames.index(i)+1).value = i #明细表表头
    for idx in sIdxes:
        rowNum = sIdxes.index(idx)+2
        dSheet.cell(rowNum,1).value = idx.name
        dSheet.cell(rowNum,2).value = idx.index
        dSheet.cell(rowNum,3).value = idx.MA250
        dSheet.cell(rowNum,4).value = idx.investmentFactor
        dSheet.cell(rowNum,5).value = idx.advanceFactor
        dSheet.cell(rowNum,6).value = idx.finalMoney
        sSheet.cell(nowSSheetRow,summarySheetRowNames.index(idx.name) + 1).value = round(idx.finalMoney,1)
    wbook.save(excelPath)
    print("ok")
def getShareData():
    print()
    data = tushare.get_hist_data('600104')
    df = tushare.pro_bar(ts_code='000001.SZ', start_date='20180101', end_date='20181011', ma=[5, 20, 50])
    print(data)
    print(df)
if __name__ == "__main__":
    rawMoney = 1000 #基准定投金额
    indexes = [
        IndexToMa250("中证500",4600,4804),
        IndexToMa250("沪深300",3633,3486),
        IndexToMa250("红利机会",7453,8142),
        IndexToMa250("深证F60",7198,6642),]
    getShareData()
    # calculateFinalMoney(indexes)
    # writeExcel(indexes)

