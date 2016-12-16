# coding=utf-8
import re
import json
import urllib.request
import pymysql.cursors


def findUsers(userName, start=0, count=1):
    name = urllib.parse.quote(userName)
    req = urllib.request.Request("https://api.douban.com/v2/user?q=%s&count=%d&start=%d" % (name, count, start))
    data = urllib.request.urlopen(req).read()
    return data.decode("utf-8")


def getConn(host='localhost',user='root',password='123456',db='world'):
    conn = pymysql.connect(host=host,
                           user=user,
                           password=password,
                           db=db,
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn;



def writeUserToDB(userList,conn,targetUserName=""):
    cursor = conn.cursor()
    for user in userList:
        print(user["name"],end=" ")
        if "loc_name" in user:
            locName = user["loc_name"]
        else:
            locName = "Unknown"
        if (targetUserName!= "") & (targetUserName!=user["name"]):
            continue
        try:
            sql = "insert into douban_user values(%d,'%s','%s','%s','%s','%s','%s')" \
                  %(int(user["id"]),user["uid"],user["name"],locName,user["created"],user["signature"],
                    user["desc"][0:100])
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print("An error: ",end="")
            print(e)

def writeAllUserToDB(conditionUserName,targetUserName=""):
    conn = getConn(db="zipkin_test")
    indexData = findUsers(conditionUserName)
    indexMap = json.loads(indexData)
    total = indexMap["total"]
    print("total "+str(total))
    for s in range(0,total,100):
        print("\n start "+str(s))
        rawData = findUsers(conditionUserName, start=s, count=100)
        rawMap = json.loads(rawData)
        allUser = rawMap["users"]
        writeUserToDB(allUser,conn,targetUserName)
    conn.close()

writeAllUserToDB("默默")

'''is_suicide: False
loc_name: 北京
large_avatar: https://img3.doubanio.com/icon/up1134011-45.jpg
uid: huangyongtao
is_banned: False
type: user
loc_id: 108288
created: 2006-04-05 20:42:24
signature: signature
avatar: https://img3.doubanio.com/icon/u1134011-45.jpg
name: Jack
alt: https://www.douban.com/people/huangyongtao/
id: 1134011
desc: descs'''