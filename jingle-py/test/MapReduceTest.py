# coding=utf-8

import functools

print("打包")

# map
res = map(lambda x: x + 1, [1, 2, 3])
print(list(res))
# 偶数
res = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
print(list(res))

# reduce 将上次迭代的结果和下一个元素作为lambda参数
res = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(res)
res = functools.reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(res)
# 如果定义一个init值,则取list中第一个值与init值作为lambda参数,否则默认取list前两个元素
res = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4], 10)
print(res)

# zip
name = ["Tom", "Nancy", "Jack"]
age = [18, 21, 34]
location = ["NY", "FRD", "SSC"]

for i in zip(name, age, location):
    print(i)


# 高阶函数
def myAdd(a, b):
    return a + b

def myAdd2(a, b, c=10):
    return a + b + c

def superAdd(f, a):
    i = 2
    return f(a, i)

print(superAdd(myAdd2, 4),end=" 高阶函数\n")

# 返回函数 使用了闭包
def superAdd2(a):
    i = 2
    def innerAdd(b=0):
        return i + a + b
    # 也可以不返回innerAdd,直接使用匿名函数如下
    # return innerAdd
    return lambda b: i + a + b

f = superAdd2(5)
print(f(6),end=" 闭包\n")

# 创建偏函数(柯里化)
myAdd3 = functools.partial(myAdd, b=3)
print(myAdd3(3),end=" 偏函数\n")
