import pymysql.cursors
import configparser

class Inserter:
    def __init__(self, confFile="conf.ini", section="local_1"):
        self.conn = self.getConnFromIniSection(confFile,section)


    def getConnFromIniSection(self,file, section):
        cf = configparser.ConfigParser()
        cf.read(file)
        return pymysql.connect(host=cf.get(section, "host"),
                               user=cf.get(section, "user"),
                               password=cf.get(section, "password"),
                               db=cf.get(section, "db"),
                               charset=cf.get(section, "charset"),
                               cursorclass=pymysql.cursors.DictCursor)

    def exe(self,sql,args=None):
        conn = self.getConnFromIniSection()
        cur = conn.cursor()
        rs = cur.execute(sql,args)
        # cur.close()
        conn.commit()
        # conn.close()
        return rs

    def exeNotCommit(self, sql, args=None):
        conn = self.getConnFromIniSection()
        cur = conn.cursor()
        rs = cur.execute(sql, args)
        return rs


    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def makeBaseSql(self, tableName):
        cur = self.conn.cursor()
        cur.execute("show columns from %s"%(tableName))
        fs =[]
        for f in cur.fetchall():
           fs.append(f["Field"])
        return self.baseSql(tableName,tuple(fs))

    def baseSql(self,table,fields):
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


    def inser(self,tableName,dataList):
        baseSql = self.makeBaseSql(tableName)
        c = self.conn.cursor()
        rs = ""
        for e in dataList:
            c.execute(baseSql,e)
            rs = c.fetchall()
        self.conn.commit()
        return rs

    def inserOne(self,sql,data):
        c = self.conn.cursor()
        c.execute(sql,data)
        rs = c.fetchall()
        self.conn.commit()
        return rs

if __name__ == "__main__":
    c = Inserter(section="local_2")
    data = [("Tom",6,"beijing"),("Jim",9,"wulumuqi")]
    c.inser("user",data)
