print('start')

#除法,整数相除/得到浮点数,//得到整数
print(1/2)
print(1//2)
print(2//3)

# 数据存储
list1 = [1, 2 , 3, 4, 5]
list1.append(6)
list1.insert(0, 0)
list1.pop(2)
print(list1)
print(list1[2])
# list生成式,10以内偶数的平方,全排列
list2 =  [x * x for x in range(1, 11) if x % 2 == 0]
list3 = [m + n for m in 'ABC' for n in 'XYZ']
print(list2)
print(list3)
# tuple is similar to list,but it can't be changed
tuple1 = (1, 2, 3)
print(tuple1)
# dictionary
dic = {'bob':12,'nacy':14,'maggie':'hoho'}
print(dic)
print(dic['bob'])
print(dic.get('bo'))
dic.pop('bob')
print(dic)
for key in dic:
    print(key)
for value in dic.values():
    print(value)
for k,v in dic.items():
    print(k,'=',v)
# set
s1 = {1,3,5,7,}
s2 = {2,4,6,7}
s3 = s1 & s2
s4 = s1 | s2
print(s3)
print(s4)
s4.add(8)
s4.remove(3)
print(s4)

# 条件
num3 = 12
if num3 < 10:
    print('num3 < 10')
    print('yeah')
elif num3 < 20:
    print('num3 > 10')
else:
    print('bigger than 20 or smaller than 10')

if 3  < 4:
    print('34')
print('43')

# 循环
for num in list1:
    num = num+1
print(list1)

sum = 0
count = 0
list100 = list(range(1001))
while sum < 10000:
    sum = sum + list100[count]
    count += 1
print('sum is not bigger than 10000 until %dth num' %count)

# 函数
def xz_add(a, b):
    # 可以返回多个值,实际上是返回一个tuple按顺序赋值到变量
    return a+b,a-b
    pass#无意义
a,b = xz_add(23,67)
print(b,a)
# 乘方递归实现,默认次数参数为2
def xz_pow(x,n=2):
    if n > 1:
        return xz_pow(x,n-1)*x
    else:
        return x
    pass
print(xz_pow(4))
# 可选可变参数
def add_some(*nums):
    sum = 0
    for n in nums:
       sum = sum + n
    return sum
print(add_some(1,2,3,))

# 其他特性
# 切片
print(list1[1:3])
print('abcde'[1:3])
# 生成器generator,类似于延迟加载
g = (x * x for x in range(10))
for n in g:
    print(n)

try:1/0
except ZeroDivisionError as e: print(e)
finally: print('continue')
try:1/0
except: print('异常')
finally: print('end')