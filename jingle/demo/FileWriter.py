# coding=utf-8

filePath = "F:/temp/test.txt"
# 写文件
file = open(filePath, "w", encoding="utf-8")
for i in range(-100, 100, 10):
    file.write(str(i) + "\n")

# 只能追加内容到开头，想追加到中间或者结尾需要把整个文件读出来，不知有没有更好的办法
# 可以使用文件指针来控制写入位置，文件打开模式会影响此方法
file = open(filePath, "w+", encoding="utf-8")
# 参数1为偏移量，参数2为初始偏移位置，0(默认)是文件开头，1是当前位置，2是文件末尾，非二进制打开只能为0
file.seek(20,2)
file.write("New thing in file\n")

# 读文件
# 默认第二个参数为r,file = open("G:/temp/test.txt","r")
file = open(filePath)
print("------------------------> file.read()")
print(file.read())
print("------------------------> for line in ")
for line in open(filePath):
    print(line)
print("------------------------> .readlines() ")
print(open(filePath).readlines())
print("------------------------> .read(100) ")
print(open(filePath).read(100))
file.close()



