# coding=utf-8

import tushare
from pylab import *
tushare.set_token('cb8ad270dcbe3411cbf4d33d2e4dd5cd026c0d015a9cd786fe218322')
mpl.rcParams['font.sans-serif'] = ['SimHei']

class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%Y-%m-%d'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        # print(x,type(x))#x在初始化图的时候是整数，当鼠标在图上移动时是浮点数
        idx = int(np.round(x))
        if idx >= len(self.dates) or idx < 0 or idx%60 !=0:
            return ''
        return self.dates[idx]

def showIndexByMA250Graph(indexName='上证指数',indexCode='000001'):
    df = tushare.pro_bar(ts_code='000300.SH', asset='I',start_date='20100101', end_date='20190929', ma=[50,250])
    print(df)
    # print(df.axes,df.columns,df.index,df.shape,df.size,
    #     sep='\n>>>----------<<<\n')
    #print(df.loc[:,['trade_date','ma50','ma250']])
    availableDf = df[0:(len(df)-250)]
    # print(availableDf)
    # data = availableDf.values
    # print(data)
    xDate = []
    yRatio = []
    for index, row in availableDf.iterrows():
        xDate.append(row['trade_date'])
        yRatio.append(row['close']/row['ma250'])
        # print(row['trade_date'],row['close'],row['ma250'],row['close']/row['ma250'])
    xDate.reverse()
    yRatio.reverse()



    fig, ax = plt.subplots(figsize=(15, 8))
    ax.xaxis.set_major_formatter(MyFormatter(xDate))# x轴坐标的刻度名字
    ax.plot(np.arange(len(xDate)), yRatio, '-')
    ax.set_title(indexName + "历年点数与年线的比值")
    ax.xaxis.grid(True, which='major') #x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='major') #y坐标轴的网格使用主刻度
    # ax.spines['bottom'].set_position(('data',1))

    plt.xticks(np.arange(0, len(xDate), 60)) #x轴刻度，起点终点和步长
    plt.yticks(np.arange(0.7, 1.8, 0.05))
    fig.autofmt_xdate()
    plt.show()

if __name__ == "__main__":
    indexs = {'300价值':'000919.SH','中证500':'000905.SH','基本面60':'399701.SZ','中证消费':'000932.SH'}
    showIndexByMA250Graph('300价值',indexs['300价值'])
    # for k,v in indexs.items():
    #     showIndexByMA250Graph(k,v)