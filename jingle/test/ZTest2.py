import pandas as pd

Cashpool = pd.read_excel(r"C:\Users\Administrator\Desktop\check.xlsm", sheet_name="3.cashpool")
lend_loan = Cashpool

def str2float(a):
    print(type(a),a,type(a)==float,type(a)==str)
    if type(a) == float or type(a) == int:
        return a
    elif type(a) == str:
        return float(a.replace(',',''))
    else:
        return 0
print(type(lend_loan))
lend_loan["Net Cash Amount"] = lend_loan["Net Cash Amount"].apply(str2float)
# lend_loan = lend_loan.loc[lend_loan["Net Cash From/To"].str.contains("To")]
# lend_loan = lend_loan[(lend_loan["Net Cash Amount"] > 0)]
print(lend_loan)
print('张景怡脑子是空的')