# coding=utf-8

import os
import re

from pylab import *

import jingle.util.MysqlConnector as JingleMysql

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定中文字体防止不显示中文


class Book:
    def __init__(self, info):
        self.id = info[0]
        self.name = info[1]
        self.time = info[2]
        self.remark = info[3]

    def store(self, dbConnector):
        bookSql = dbConnector.makeBaseSql("book")
        print((self.id, self.name, self.time, self.remark))
        # dbConnector.insertOne(bookSql,(self.id,self.name,self.time,self.remark))


class Student:
    def __init__(self, number, name):
        self.id = number
        self.name = name

    def store(self, dbConnector):
        userSql = dbConnector.makeBaseSql("user")
        dbConnector.insertOne(userSql, (self.id, self.name, self.id[:7], ''))


def getLines(fileName, student):
    file = open(fileName, 'r', encoding="utf8")
    lines = file.readlines()
    for line in lines:
        if line != '\n' and line.find('序号') < 0:
            info = line.replace("\n", "").replace("\"", "").split(",")
            yield ("%s-%s-%s" % (student.id, info[4], info[0]),
                   info[0],
                   info[3],
                   info[2].replace(r".", "-"),
                   info[1][2:],
                   student.id,
                   student.name)


def insertBookInfo(path):
    inserter = JingleMysql.Inserter("conf.ini", "local_2")
    files = os.listdir(path)
    p1 = re.compile(r'\d{9}')
    p2 = re.compile(r'[\u4e00-\u9fa5]{2,3}')
    for fileName in files:
        studentId = re.search(p1, fileName).group()
        studentName = re.search(p2, fileName).group()
        student = Student(studentId, studentName)
        try:
            student.store(inserter)
        except Exception as e:
            print(e)
        try:
            books = list(getLines(path + fileName, student))
            print("%s has %s records" % (student.name, len(books)))
            inserter.insert("book", books)
        except Exception as e:
            print(e)


class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%Y-%m-%d'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        idx = int(np.round(x))
        if idx >= len(self.dates) or idx < 0:
            return ''
        return self.dates[idx]


def findName(finder, userId):
    return finder.find("select name from user where id = %s" % userId).__next__()["name"]


def findBooks(finder, userId):
    myBooks = list(finder.find("select DATE_FORMAT(time,'%%Y%%m') months,count(*) count from book "
                               "where user_id=%s group by months;" % userId))
    x = list(i['months'] for i in myBooks)
    y = list((int(i['count']) // 2) for i in myBooks)
    return x, y


def showBooks(userId, monthStep=1, yHeight=20):
    finder = JingleMysql.Finder("conf.ini", "local_2")
    x, y = findBooks(finder, userId)
    if len(x) <=0:
        print("学号 %s 的数据不存在"% userId)
        return
    # fig, axes = plt.subplots(ncols=2,figsize=(10, 30))
    # ax = axes[0]
    fig, ax = plt.subplots(figsize=(15, 4))
    formatter = MyFormatter(x)
    ax.xaxis.set_major_formatter(formatter)
    ax.plot(np.arange(len(x)), y, 'o--')
    ax.set_title("[%s]在广金的借书情况"%findName(finder, userId))

    plt.xticks(np.arange(0, len(x), monthStep))
    plt.yticks(np.arange(0, yHeight, 5))
    fig.autofmt_xdate()
    plt.show()


if __name__ == '__main__':
    print("start")
    # insertBookInfo('net/books/')

    [showBooks(i) for i in range(121542345,121542346)]