# coding utf-8
# 选取几个指数, 计算它们年线与当天数值的差距, 将所有差距加和乘以3再加一百, 作为总金额投资系数,即将差距放大三倍
# 总金额投资系数乘以原投资金额,作为计划投资金额
# 以最低的差距作为0, 其他差距减去最低差距作为权重, 算出所有指数占总投资金额的百分比
# 将百分比乘以计划投资金额, 得出各指数投入金额
import xlrd,xlwt,time

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
    wbook = None
    excelPath = '../resource/定投记录.xls'
    nowDateStr = time.strftime("%Y-%m-%d", time.localtime())
    totalMoney = 0
    detailSheetRowNames = ["指数名","指数值","年线","偏离程度","投资因子","投资金额"]
    summarySheetRowNames = ["年月","总金额"]#汇总表的各列名
    for i in sIdxes:
        summarySheetRowNames.append(i.name)
        totalMoney = totalMoney + i.finalMoney
    try:
        wbook = xlrd.open_workbook(excelPath)
    except FileNotFoundError as e:
        wbook = xlwt.Workbook()
        # 表头列名
        sSheet = wbook.add_sheet(time.strftime("%Y", time.localtime()))
        dSheet = wbook.add_sheet(nowDateStr)
        for i in summarySheetRowNames: sSheet.write(0,summarySheetRowNames.index(i),i) #行 列 内容
        for i in detailSheetRowNames: dSheet.write(0,detailSheetRowNames.index(i),i)
        wbook.save(excelPath)
    wbook = xlrd.open_workbook(excelPath)
    sSheet = wbook.sheets()[0]
    dSheet = wbook.sheet_by_name(nowDateStr)
    print(dSheet.name)
    for idx in sIdxes:
        print(idx.name,sIdxes.index(idx))
        dSheet.put_cell(sIdxes.index(idx),0,1,idx.name,0)
        dSheet.put_cell(sIdxes.index(idx),1,1,idx.index,0)
        dSheet.put_cell(sIdxes.index(idx),2,1,idx.MA250,0)
        dSheet.put_cell(sIdxes.index(idx),3,1,idx.investmentFactor,0)
        dSheet.put_cell(sIdxes.index(idx),4,1,idx.advanceFactor,0)
        dSheet.put_cell(sIdxes.index(idx),5,1,idx.finalMoney,0)
    dSheet.put_cell(0, 0, 1, "米", 0)
    print(dSheet.cell(0,0).value)
    # wbook.save(excelPath)
    print("ok")

if __name__ == "__main__":
    rawMoney = 1000 #基准定投金额
    indexes = [
        IndexToMa250("中证500",4600,4804),
        IndexToMa250("沪深300",3633,3486),
        IndexToMa250("红利机会",7453,8142),
        IndexToMa250("深证F60",7198,6642),]
    # calculateFinalMoney(indexes)
    writeExcel(indexes)

