#coding=utf-8
import os

print("ok")
file = open("G:/temp/test.txt","w", encoding="utf-8")
for i in range(-100,100,10):
    file.write(str(i)+"\n")

file = open("G:/temp/test.txt","w+", encoding="utf-8")
file.write("New thing in file")

#默认第二个参数为r,file = open("G:/temp/test.txt","r")
file = open("G:/temp/test.txt")
print(file.read())
for line in open("G:/temp/test.txt"):
    print(line)
print(open("G:/temp/test.txt").readlines())
print(open("G:/temp/test.txt").read(100))
file.close()
print("file finish")

str1 = os.system('ls /')
print(str1)

f = file("G:/temp/test.txt")
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line) # notice comma
f.close()