#coding=utf-8
import os

# -*- coding: cp936 -*-
import os
path = "F:\\audio\手机录音\\records_former\\六级听力\\"
prefix = "亚纪录音_"
fileList = os.listdir(path)
for file in fileList:
    if file.find(".")>-10:
        newName = prefix + str(fileList.index(file))+".mp3"
        print(newName)
        print(fileList.index(file))
        try:
            os.rename(path + file,path + newName)
        except Exception as e:
            print(e)

for file in os.listdir(path):
    print(file)

print(len(fileList))