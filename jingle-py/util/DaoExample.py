# coding=utf-8
import util.MysqlConnector as dao

ins = dao.Inserter()
tp = (1215123,"tom",3,"伦敦")
ins.insert("student",[tp])

fin = dao.Finder()
for s in fin.findAll("student"):
    print(s)

