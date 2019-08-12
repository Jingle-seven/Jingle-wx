# coding utf-8
# 选取几个指数, 计算它们年线与当天数值的差距, 将所有差距加和乘以3再加一百, 作为总金额投资系数,即将差距放大三倍
# 总金额投资系数乘以原投资金额,作为计划投资金额
# 以最低的差距作为0, 其他差距减去最低差距作为权重, 算出所有指数占总投资金额的百分比
# 将百分比乘以计划投资金额, 得出各指数投入金额

class IndexToMa250:
    def __init__(self, name, index, MA250):
        self.name = name
        self.index = index
        self.MA250 = MA250
        self.investmentFactor = self.MA250*100/self.index - 100
        self.advanceFactor = 0
        self.advancePercentage = 0


rawMoney = 1000 #基准定投金额
indexes = [
    IndexToMa250("中证500",4600,4804),
    IndexToMa250("沪深300",3633,3486),
    IndexToMa250("红利机会",7453,8142),
    IndexToMa250("深证F60",7198,6642),]

lowestIdx = indexes[0] #最low的指数
totalInvestmentFactor = 0 #第一投资系数,用于计算总投资
totalFactor = 0 #第二投资系数,用于计算各指数投资占比
for i in indexes: #加和第一投资系数(用于计算总投资金额),并找出最小的投资系数
    totalInvestmentFactor = totalInvestmentFactor + i.investmentFactor
    if i.investmentFactor < lowestIdx.investmentFactor:
        lowestIdx = i

print("最小系数:\t\t %.2f %s" % (lowestIdx.investmentFactor,lowestIdx.name))
#汇总所有指数减去最小投资系数后的值(即计划投资系数),得到总计划投资系数.
# 也就是说,最小的那个指数, 投资0元. 以此指数为基础,偏离越大投资占比越大
for i in indexes:
    i.advanceFactor = i.investmentFactor - lowestIdx.investmentFactor
    totalFactor = totalFactor + i.advanceFactor
for i in indexes: #每个指数计划投资系数除以第二系数,得到每个指数占总投资金额的百分比
    i.advancePercentage = i.advanceFactor / totalFactor

print("总定投系数:\t\t %.2f"%totalInvestmentFactor)

# 系数放大三倍,也就是以当天所有指数平均值为基准,如果年线在平均值66%则停止定投,年线在133%时加倍定投,166%时3倍定投
planMoney = rawMoney * (totalInvestmentFactor*3 +100) /100

print("计划定投金额:\t %.2f"%planMoney)
# print("总定投系数", divideByFactor)
for i in indexes:
    print("%s:\t %.2f"% (i.name,i.advancePercentage * planMoney))

