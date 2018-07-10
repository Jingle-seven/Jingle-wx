# coding=utf-8
from . import MysqlConnector

ins = MysqlConnector.Inserter()
tp = (1215123,"tom",3,"伦敦")
ins.insert("student",[tp])

fin = MysqlConnector.Finder()
for s in fin.findAll("student"):
    print(s)

