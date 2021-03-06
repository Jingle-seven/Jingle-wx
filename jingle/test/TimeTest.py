import time
import datetime # datetime提供了基于time的更多方法
import calendar

# 时间戳
timeStamp = time.time()
print(timeStamp)

# 标准时间元组
localTime = time.localtime()
print(localTime)

# 日期时间加减
dt = datetime.datetime.now()
print(dt,dt.day)
dt = dt + datetime.timedelta(days=1)
print(dt,dt.strftime("%Y-%m-%d"))

# 字符串转datetime
dt2 = datetime.datetime.strptime('20200129','%Y%m%d')
print(dt2)

# 简单的可视时间 Thu Feb  6 10:09:08 2020
ascTime = time.asctime()
print(ascTime)

# 格式化时间
strTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(strTime)

# 格式化时间转时间戳
timeArray = time.strptime('09-15-2017 17:53:45', "%m-%d-%Y %H:%M:%S")
timestamp = time.mktime(timeArray)
print(timestamp)

# 输出一个月的日历
cal = calendar.month(2016, 10)
print(cal)

print ("本地时间为 :", time.asctime(),time.ctime())
print ("格式化的时间 :",time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime()))
print ("以下输出2016年1月份的日历:\n",calendar.month(2016, 1))