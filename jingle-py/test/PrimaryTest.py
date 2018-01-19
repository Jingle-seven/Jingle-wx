# print函数的参数可以由逗号分隔，会自动连接
start = 0
end = 10
print("start=", start)
print('next')

# 除法,整数相除/得到浮点数,//得到整数
print(1 / 2)
print(1 // 2)
print(2 // 3)

# 数据存储
list1 = [1, 2, 3, 4, 5]
list1.append(6)
list1 +=[7]
list1.insert(0, 0)
list1.pop(2)
print("LIST ----------------------> ",list1)
print(list1[2])
# list生成式,10以内偶数的平方,全排列
list2 = [x * x for x in range(1, 11) if x % 2 == 0]
list3 = [m + n for m in 'ABC' for n in 'XYZ']
print(list2)
print(list3)
# tuple is similar to list,but it can't be changed
tuple1 = (1, 2, 3)
print(tuple1)
# dictionary
dic = {'bob': 12, 'nancy': 14, 'maggie': 'hoho'}
print("DIC ----------------------> ",dic)
print(dic['bob'])
print(dic.get('bo'))
dic.pop('bob')
print(dic)
for key in dic:
    print(key)
for value in dic.values():
    print(value)
for k, v in dic.items():
    print(k, '=', v)
# set
s1 = {1, 3, 5, 7, }
s2 = {2, 4, 6, 7}
s3 = s1 & s2
s4 = s1 | s2
print("SET ----------------------> ",s3)
print(s4)
s4.add(8)
s4.remove(3)
print(s4)

#输出格式化及字符串方法
print("FORMAT ----------------------> ")
print("format {} and {}".format("A","B"))
print("format {who} and {me}".format(who="Bob",me="Nancy"))
print("format {0[0]} and {0[1]}".format(list1))
print("format {0[maggie]} and {0[nancy]}".format(dic))
print("format {maggie} and {maggie}".format(**dic))
print("format {start} and {end}".format(**locals()))# 甚至可以用locals将局部变量传入
print("abc".find("x"))
print("abcabc".replace("c","d",1))
print("a b c".split(" ",1))

# 条件
print("CONDITION ----------------------> ")
num3 = 12
if num3 < 10:
    print('num3 < 10')
    print('yeah')
elif num3 < 20:
    print('num3 > 10')
else:
    print('bigger than 20 or smaller than 10')
# None/空序列或集合/0等数据项的布尔值为False
condition = {}
if condition:
    print("true")
else:
    print("false")
# 返回操作数而非布尔值
print(2 and 5)
print(2 and 0)

# 循环
print("LOOP ----------------------> ")
for num in list1:
    num = num + 1
print(list1)

sum = 0
count = 0
list100 = list(range(1001))
while sum < 10000:
    sum = sum + list100[count]
    count += 1
print('sum is not bigger than 10000 until %dth num' % count)


# 函数
def xz_add(a, b):
    # 可以返回多个值,实际上是返回一个tuple按顺序赋值到变量
    return a + b, a - b
    pass  # 无意义
a, b = xz_add(23, 67)
print(b, a)

# 乘方递归实现,默认次数参数为2
def xz_pow(x, n=2):
    if n > 1:
        return xz_pow(x, n - 1) * x
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
print(add_some(1, 2, 3, ))

# 其他特性
# 切片
print(list1[1:3])
print('abcde'[1:3])
# 生成器generator,类似于延迟加载
g = (x * x for x in range(10))
x = [x * x for x in range(1, 11) if x % 2 == 0]
for n in g:
    print(n,end=" ")

try:
    1 / 0
except ZeroDivisionError as e:
    print(e)
finally:
    print('continue')
try:
    1 / 0
except:
    print('异常')
finally:
    print('end')
