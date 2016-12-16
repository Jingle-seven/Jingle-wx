#coding=utf-8

import time
import calendar

print ("本地时间为 :", time.asctime(),time.ctime())
print ("格式化的时间 :",time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime()))
print ("以下输出2016年1月份的日历:\n",calendar.month(2016, 1))