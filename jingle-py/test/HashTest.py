# conding=utf-8

for i in range(100,1000,3):
    num = 15
    print("%s mod\n%s: \n%s\n"%(bin(i)[2:],bin(num)[2:],bin(i&num)[2:]))