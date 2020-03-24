#coding=utf-8
import hashlib,os,re
path = "D:/迅雷下载/画画/"

fileList = os.listdir(path)
fileMD5ToSize = {}
delCounter = 0
bookCounter = 0
for fileName in fileList:
    bookCounter +=1
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
        # os.remove(path + fileName)
        delCounter +=1
        continue
    else:
        fileMD5ToSize[fileMD5] = fileSize
    # x = re.sub(r'[^\D]+\.pdf','',fileName)
    # x = x.replace(" ","").replace("+","")
    x = fileName.replace('.pdf.pdf','')
    try:
        fullName = path + x
        # print(x)
        if  '.pdf' not in fullName:
            fullName = fullName + '.pdf'
            print(fullName)
        os.rename(path+fileName,fullName)
    except FileExistsError as e:
        print(x)
        continue

# print(fileMD5ToSize)
print("delete %d files"% delCounter)