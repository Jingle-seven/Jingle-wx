import demo.BaseDao as dao
import demo.MysqlConnector.Inserter as Inserter
import demo.JingleUtil as util
import time
import random

spans = ("span1", "span2", "span3", "span4")
hosts = ("127.0.0.1","127.0.0.2","127.0.0.55","127.0.0.60")
traceMd5s = ("abc", "aaa", "cba")
staSpanFs = ("id", "start_time", "end_time", "span_name", "called_num", "avg_time", "slowest_id", "slowest_time", "slowest_host")
traceFs = ("trace_id","trace_md5","start_ts","duration","end_ts","team_code")
spanFs = ("trace_id","span_id","endpoint_ipv4","endpoint_service_name","start_ts","duration","record_ts",)

connector = Inserter("conf.ini","local_1")
staSpanSql = connector.makeBaseSql("statistics_spans")
tracesSql = connector.makeBaseSql("traces")
spansSql = connector.makeBaseSql("spans")
# print(baseSql)


for i in range(10, 20):
    etime = int(time.time()*1000)
    stime = etime - 10 * 1000
    spanName = random.choice(spans)
    callNum = random.randint(10,50)
    avgTime = random.randint(4,20)
    tsId = random.randint(1400000000000, 1500000000000)
    slowTime = random.randint(25,50)
    ipv4 = random.choice(hosts)
    duration = random.randint(100,200)
    traceMd5 = random.choice(traceMd5s)
    try:
        connector.inserOne(tracesSql,(tsId,traceMd5,stime,duration,stime+duration,0))
        spanNum = random.randint(2,5)
        for j in range(1,spanNum):
            connector.inserOne(spansSql,(tsId,tsId+j*100,util.ipTpInt(ipv4),spanName,stime,duration/spanNum,time.time()))
        # connector.inserOne(staSpanSql, (i, stime, etime, spanName, callNum, avgTime, tsId, slowTime, slowHost))
    except Exception as e:
        print(e)


print("finished !")
