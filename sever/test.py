import os
import django

cs = [":","<",">","\\","/","?",'"',"*","|"]
str = "job_1481246310720_0452-1481357273822-xiangy-Distributed+Lzo+Indexer+%5B%2FDATA%2FETL%2FTMP_SUBJECT_ADP-1481357300332-481-0-SUCCEEDED-root.xiangy-1481357284713.jhist"
for c in cs:
    if str.find(c)>0:
        print(c)
print(len(cs))


