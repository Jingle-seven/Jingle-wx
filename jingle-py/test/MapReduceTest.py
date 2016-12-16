#coding=utf-8

import functools
print("打包")

#map
res = map(lambda x: x+1,[1,2,3])
print(list(res))
#偶数
res = filter(lambda x: x%2==0,[1,2,3,4])
print(list(res))

#reduce 将上次迭代的结果和下一个元素作为lambda参数
res = functools.reduce(lambda x,y: x+y,[1,2,3,4])
print(res)
res = functools.reduce(lambda x,y: x*y,[1,2,3,4])
print(res)
#如果定义一个init值,则取list中第一个值与init值作为lambda参数,否则默认取list前两个元素
res = functools.reduce(lambda x,y: x+y,[1,2,3,4],10)
print(res)

#zip
name = ["Tom","Nancy","Jack"]
age = [18,21,34]
location = ["NY","FRD","SSC"]

for i in zip(name,age,location):
    print(i)


