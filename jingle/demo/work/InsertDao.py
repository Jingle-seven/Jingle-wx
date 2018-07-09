import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='127.0.0.1',
                       user='xjh',
                       password='z',
                       db='cloudins_junit',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()
insertSql = "insert into cloudins_user(role_id,field_id,account,name,password,gender,mail,company,phone,qq,status,remark) " \
               "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

cur.execute(insertSql, ("1", "1215", "Nancy@qq.com", "Nancy", "Nancy", "0", "Nancy@qq.com", "GDUF", "13600000", "82000", "", "南希"))
cur.execute(insertSql, ("1", "1215", "Nancy@qq.com", "Nancy", "Nancy", "0", "Nancy@qq.com", "GDUF", "13600000", "82000", "", "南希妹妹"))

# conn.commit()
cur.close()
conn.close()

def makeBaseSql(table, fields):
    sqlP1 ="insert into %s("%(table)
    sqlP2 = ") values("
    if isinstance(fields, tuple):
        for field in fields:
            sqlP1 = sqlP1 + field + ","
            sqlP2 = sqlP2 + "%s,"
    elif isinstance(fields, dict):
        for (k,v) in fields.items():
            sqlP1 = sqlP1 + k + ","
            sqlP2 = sqlP2 + str(v) + ","
    else:
        raise Exception("rows should be a tuple or dict")
    sqlP1 = sqlP1[0:len(sqlP1)-1]
    sqlP2 = sqlP2[0:len(sqlP2)-1]

    resSql = sqlP1 + sqlP2 + ")"
    return resSql

def makeExeSql(table,fields,data):
    theSql = makeBaseSql(table,fields)
    resSql = theSql%data
    return resSql

def fillBaseSql(baseSql,data):
    return baseSql % data

sql = makeBaseSql("spans", ("trace_id", "id", "time"))
sql = fillBaseSql(sql,(2,4,148))
print(sql)
m = {"trace_id":1,"id":2,"time":148}
print(makeBaseSql("span",m))
