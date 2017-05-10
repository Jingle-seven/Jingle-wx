# coding=utf-8

import random
def getRandList():
    for i in range(10):
        yield random.randint(10,20)

list = list(getRandList())
print(list)