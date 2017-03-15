import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='10.17.36.55',
                       user='root',
                       password='z',
                       db='cloudins',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()
cur.execute("SELECT * FROM zipkin_spans")
traceIds = set()
appIds = set()
for r in cur.fetchall():
    traceId = int(r["trace_id"])
    traceIds.add(traceId)

'''application_1475907758598_12314'''
cur.execute("SELECT * FROM yarn_app_result ")
for r in cur.fetchall():
    preAppId = int(r["id"][12:25])
    sufAppId = int(r["id"][26:31])
    appIds.add(preAppId*10000 + sufAppId)
cur.close()
conn.close()

print(len(traceIds))
print(len(appIds))
errorIds = set()
for appId in appIds:
    if appId not in traceIds:
        print(appId)
        errorIds.add(appId)

print(len(errorIds))
