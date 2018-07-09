#coding=utf-8
import os

# -*- coding: cp936 -*-
import os
path = "F:\\DOC\\desktop\\CustomEmotions\\"
prefix = "亚纪录音_"
counter = 0

def codition(fileName):
    return fileName.find(".") < 0

fileList = os.listdir(path)
for file in fileList:
    if codition(file):
        # newName = prefix + str(fileList.index(file))+".mp3"
        newName = str(file)[:15]+".gif"
        try:
            os.rename(path + file,path + newName)
            print("%s renamed to %s"%(str(file),newName))
            counter+=1
        except Exception as e:
            print(e)

# for file in os.listdir(path):
#     print(file)

print("rename %d files"% counter)