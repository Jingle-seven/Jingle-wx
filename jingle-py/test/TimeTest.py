import time
import calendar

timeStamp = time.time()
print(timeStamp)

localTime = time.localtime()
print(localTime)

ascTime = time.asctime()
print(ascTime)

strTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(strTime)

cal = calendar.month(2016, 10)
print(cal)

sTime = time.clock()
time.sleep(2)
eTime = time.clock()
print(eTime-sTime)