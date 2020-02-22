# 不能获取沪深300估值数据，辣鸡
import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond:'+lg.error_code)
print('login respond :'+lg.error_msg)

#### 获取历史K线数据 ####
# 沪深A股估值指标(日频) 示例
rs = bs.query_history_k_data_plus("sh.000300","date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM",
    start_date='2019-01-01', end_date='2019-12-31', frequency="d", adjustflag="3")
print('respond:'+rs.error_code)
print('respond :'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
print(rs.fields)
print(data_list)
#### 结果集输出到csv文件 ####
# result.to_csv("D:/history_k_data.csv", encoding="gbk", index=False)
# print(result)

#### 登出系统 ####
bs.logout()