# coding=utf-8
# 将指定目录下的所有子孙文件移动到这个目录下
import os
import shutil

basePath = "F:/temp/test"

# 递归列出指定目录下所有文件
def listFiles(path):
    pathToFile={}
    subFiles = os.listdir(path)
    for fileName in subFiles:
        filePath = os.path.join(path,fileName)
        # print(file)
        if os.path.isdir(filePath):
            pathToFile.update(listFiles(filePath))
        # 根目录下的文件忽略
        elif path != basePath:
            pathToFile[filePath] = fileName
    return pathToFile
# 其实这个方法可以用以下方法代替：
# for root,dirs,files in os.walk(dir):
#     for file in files:
#         print(os.path.join(root,file))

for k,v in listFiles(basePath).items():
    # print("{} \t\t {}".format(k,v))
    # pathFile = os.path.split(k)
    print("move [{}] ----------------> [{}]".format(k,os.path.join(basePath,v)))
    # 此方法会把同名文件覆盖
    shutil.move(k,os.path.join(basePath,v))
