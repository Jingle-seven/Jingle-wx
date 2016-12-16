import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='127.0.0.1',
                       user='xjh',
                       password='z',
                       db='cloudins',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()
cur.execute("SELECT * FROM yarn_app_result order by start_time")
targetOrderField = []
for r in cur.fetchall():
    appId = int(r["id"][26:31])
    recordTs = r["record_ts"]
    targetOrderField.append(recordTs)
    cur.close()
conn.close()

'''application_1475907758598_12314'''
print(len(targetOrderField))
count = 0
for i in range(0, len(targetOrderField) - 1):
    if targetOrderField[i] > targetOrderField[i + 1]:
        print(targetOrderField[i - 1])
        print(targetOrderField[i])
        print(targetOrderField[i + 1])
        print("wrong order %d" % (i))
        count += 1

print("total wrong order: %d" % count)

# for s in startTimes:
#     print(s)
