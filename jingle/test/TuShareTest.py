import tushare
tushare.set_token('cb8ad270dcbe3411cbf4d33d2e4dd5cd026c0d015a9cd786fe218322')

df = tushare.pro_bar(ts_code='000300.SH', asset='I',start_date='20170101', end_date='20190101', ma=[50,250])
print(df.columns)
print(df.index)
print(df.values)
#print(df.loc[:,['trade_date','ma50','ma250']])