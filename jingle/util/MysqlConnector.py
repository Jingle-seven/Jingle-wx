import pymysql.cursors
import configparser


class Inserter:
    def __init__(self, confFile="../resource/conf.ini", section="local_2"):
        self.conn = self.getConnFromIniSection(confFile, section)

    def getConnFromIniSection(self, file, section):
        cf = configparser.ConfigParser()
        cf.read(file)
        return pymysql.connect(host=cf.get(section, "host"),
                               user=cf.get(section, "user"),
                               password=cf.get(section, "password"),
                               db=cf.get(section, "db"),
                               charset=cf.get(section, "charset"),
                               cursorclass=pymysql.cursors.DictCursor)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def makeBaseSql(self, tableName):
        cur = self.conn.cursor()
        cur.execute("show columns from %s" % (tableName))
        fs = []
        for f in cur.fetchall():
            fs.append(f["Field"])
        return self.baseSql(tableName, tuple(fs))

    def baseSql(self, table, fields):
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

    def insert(self, tableName, dataList):
        baseSql = self.makeBaseSql(tableName)
        c = self.conn.cursor()
        rs = ""
        for e in dataList:
            c.execute(baseSql, e)
            rs = c.fetchall()
        self.conn.commit()
        return rs

    def insertOne(self, sql, data):
        c = self.conn.cursor()
        c.execute(sql, data)
        rs = c.fetchall()
        self.conn.commit()
        return rs


class Finder:
    def __init__(self, confFile="../resource/conf.ini", section="local_2"):
        self.conn = self.getConnFromIniSection(confFile, section)

    def getConnFromIniSection(self, file, section):
        cf = configparser.ConfigParser()
        cf.read(file)
        return pymysql.connect(host=cf.get(section, "host"),
                               user=cf.get(section, "user"),
                               password=cf.get(section, "password"),
                               db=cf.get(section, "db"),
                               charset=cf.get(section, "charset"),
                               cursorclass=pymysql.cursors.DictCursor)

    def findAll(self, table):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM %s " % table)
        for r in cur.fetchall():
            yield r

    def find(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        for r in cur.fetchall():
            yield r


if __name__ == "__main__":
    c = Inserter(section="local_2")
    data = [("Tom", 6, "beijing"), ("Jim", 9, "wulumuqi")]
    c.insert("user", data)
