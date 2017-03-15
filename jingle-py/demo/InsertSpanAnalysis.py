import demo.BaseDao as dao
import time
import random

spans = ("span1", "span2", "span3", "span4")
hosts = ("127.0.0.1","127.0.0.2","127.0.0.55","127.0.0.60")
fs = ("id", "start_time", "end_time", "span_name", "called_num", "avg_time", "slowest_id", "slowest_time", "slowest_host")
baseSql = dao.makeBaseSql("statistics_spans", fs)
# print(baseSql)


for i in range(10, 20):
    etime = int(time.time()*1000)
    stime = etime - 10 * 1000
    spanName = random.choice(spans)
    callNum = random.randint(10,50)
    avgTime = random.randint(4,20)
    slowId = random.randint(1400000000000,1500000000000)
    slowTime = random.randint(25,50)
    slowHost = random.choice(hosts)
    dao.exe(baseSql, (i, stime, etime,spanName, callNum, avgTime, slowId, slowTime, slowHost))
