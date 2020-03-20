#coding=utf-8
import hashlib
import os
path = "C:/Users/Administrator/Desktop/test/"

fileList = os.listdir(path)
fileMD5ToSize = {}
delCounter = 0
for fileName in fileList:
    if os.path.isdir(path + fileName):continue #跳过目录
    midName = str(fileList.index(fileName))
    headBits = open(path + fileName, "rb").read(10000)
    md5 = hashlib.md5()
    md5.update(headBits)
    fileMD5 = md5.hexdigest()
    fileSize = os.path.getsize(path + fileName)
    # MD5一样，大小一样，说明是重复，删除之
    if fileMD5 in fileMD5ToSize and fileMD5ToSize[fileMD5] == fileSize:
        print('delete '+fileName)
        os.remove(path + fileName)
        delCounter +=1
    else:
        fileMD5ToSize[fileMD5] = fileSize
    if '、' in fileName:
        newName = fileName.split('、')[1]
        os.rename(path+fileName,path + newName)

# print(fileMD5ToSize)
print("delete %d files"% delCounter)