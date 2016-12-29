import time
import calendar

# 时间戳
timeStamp = time.time()
print(timeStamp)

# 标准时间元组
localTime = time.localtime()
print(localTime)

# 简单的可视时间
ascTime = time.asctime()
print(ascTime)

# 格式化时间
strTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(strTime)

# 输出一个月的日历
cal = calendar.month(2016, 10)
print(cal)

# 第一次调用返回时间戳,第二次返回与第一次的间隔
sTime = time.clock()
time.sleep(2)
eTime = time.clock()
print(eTime-sTime)