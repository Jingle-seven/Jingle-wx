#coding=utf-8
import os

# -*- coding: cp936 -*-
import os
path = "G:\\xunlei\\net-photo\\Menhera-chan - SR汉化"
prefix = "menhera-"
midName = ""
suffix = ".jpg"
counter = 0

def condition(fileName):
    return fileName.find(".") != 0

fileList = os.listdir(path)
print(fileList)
for file in fileList:
    midName = str(fileList.index(file))
    if condition(file):
        newName = prefix + midName + suffix
        print(newName)
        try:
            os.rename(path+"/"+file,path +"/"+ newName)
            print("%s > %s"%(str(file),newName))
            counter+=1
        except Exception as e:
            print(e)

# for file in os.listdir(path):
#     print(file)

print("rename %d files"% counter)