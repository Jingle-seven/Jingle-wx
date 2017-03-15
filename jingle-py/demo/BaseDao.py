import pymysql.cursors
import configparser


def getConnFromIniSection(file="conf.ini", section="mysql"):
    cf = configparser.ConfigParser()
    cf.read(file)
    return pymysql.connect(host=cf.get(section, "host"),
                           user=cf.get(section, "user"),
                           password=cf.get(section, "password"),
                           db=cf.get(section, "db"),
                           charset=cf.get(section, "charset"),
                           cursorclass=pymysql.cursors.DictCursor)


def makeBaseSql(table, fields):
    sqlP1 = "insert into %s(" % (table)
    sqlP2 = ") values("
    if isinstance(fields, tuple):
        for field in fields:
            sqlP1 = sqlP1 + field + ","
            sqlP2 = sqlP2 + "%s,"
    elif isinstance(fields, dict):
        for (k, v) in fields.items():
            sqlP1 = sqlP1 + k + ","
            sqlP2 = sqlP2 + str(v) + ","
    else:
        raise Exception("rows should be a tuple or dict")
    sqlP1 = sqlP1[0:len(sqlP1) - 1]
    sqlP2 = sqlP2[0:len(sqlP2) - 1]

    resSql = sqlP1 + sqlP2 + ")"
    return resSql


def fillBaseSql(baseSql, data):
    return baseSql % data


def makeExeSql(table, fields, data):
    theSql = makeBaseSql(table, fields)
    resSql = theSql % data
    return resSql

def exe(sql,args=None):
    conn = getConnFromIniSection()
    cur = conn.cursor()
    rs = cur.execute(sql,args)
    # cur.close()
    conn.commit()
    conn.close()
    return rs

if __name__ == "__main__":
    print("main")
    cf = configparser.ConfigParser()
    cf.read("conf.ini")

    print(cf.sections())
    print(cf.items("mysql"))
    print(cf.options("mysql"))
    print(cf.get("mysql", "db"))
    print(cf.getint("mysql", "port"))
    print(cf.getfloat("mysql", "port"))
    print(cf.getboolean("mysql", "useSSL"))
