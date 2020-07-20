import pandas as pd
from locale import *

Cashpool=pd.read_excel(r"C:\Users\Administrator\Desktop\check.xlsm",sheet_name="3.cashpool")
def str2float(a):
 if "," in a:
    setlocale(LC_NUMERIC, 'English_US')
    return atof(a)
 elif type(a)==float:
    return a
 else:
    return float(a)
print(type(Cashpool))
Cashpool["EOD Value Balance"] = Cashpool["EOD Value Balance"].apply(str2float)
CashpoolBalance=Cashpool.loc[:,["Account Number","EOD Value Balance","Net Cash From/To"]]
CashpoolBalance=CashpoolBalance[(Cashpool["EOD Value Balance"]>0)]
CashpoolBalance=CashpoolBalance.loc[:,["Account Number","EOD Value Balance","Net Cash From/To"]]
# print(CashpoolBalance)#输出非lend loan的balance结果