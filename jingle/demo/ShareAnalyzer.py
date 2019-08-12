# coding=utf-8
import time

# 周几:[上涨次数,下跌次数,波动总金额]
wDayToInfo = {0:[0,0,0],1:[0,0,0],2:[0,0,0],3:[0,0,0],4:[0,0,0],5:[0,0,0],6:[0,0,0]}
fileName = 'sh000905.csv'
file = open('../resource/share/'+fileName, 'r', encoding="utf8")
lines = file.readlines()
for i,line in enumerate(lines):
    # if i>5: break
    if i==0: continue
    info = line.replace("\n", "").replace("\'", "").split(",")
    timeTuple = time.strptime(info[0], "%Y-%m-%d")
    # print(info)
    # print(timeTuple.tm_wday)
    # print(info[0],timeTuple.tm_wday)
    amount = 0
    if info[8]!= 'None': amount = float(info[8])# 涨跌数字
    wDayToInfo[timeTuple.tm_wday][2] = wDayToInfo[timeTuple.tm_wday][2] + amount
    if info[9]!= 'None': amount = float(info[9])# 涨跌幅度
    if amount >0:
        wDayToInfo[timeTuple.tm_wday][0]+=1
    else:
        wDayToInfo[timeTuple.tm_wday][1]+=1
    if i==1: print(info[2])# 股票名

# print(wDayToInfo)
for (k,v) in wDayToInfo.items():
    print('星期%s涨了%s次,跌了%s次,总波动数字 %.2f'%(k+1,v[0],v[1],v[2]))