start = 0
end = 10
list1 = [1, 2, 3, 4, 5]
dic = {'bob': 12, 'nancy': 14, 'maggie': 'hoho'}
# print函数有一个变长参数和seq（分隔符，默认空格）、end（结尾符，默认换行）、file（输出到哪，默认控制台）三个关键字参数
print("start=", start)
print('next')

# 除法,整数相除/得到浮点数,//得到整数
print(1 / 2)
print(1 // 2)
print(2 // 3)

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

theSum = 0
count = 0
list100 = list(range(1001))
while theSum < 10000:
    theSum += list100[count]
    count += 1
print('sum is not bigger than 10000 until %dth num' % count)


# 函数
def xz_add(a, b):
    # 可以返回多个值,实际上是返回一个tuple按顺序赋值到变量
    return a + b, a - b
    pass  # 无意义
# 调用函数时可以用*将元组或者列表绑定到位置参数，用**绑定dict和关键字参数
tp = tuple(list1[:2])
a, b = xz_add(*tp)
print(b, a)

# 乘方递归实现,默认次数参数为2
def xz_pow(x, n=2):
    if n > 1:
        return xz_pow(x, n - 1) * x
    else:
        return x
    pass
print(xz_pow(4))

# 数量可变的位置参数
def add_some(who ,*nums):
    mySum = 0
    for n in nums:
        mySum = mySum + n
    return who + str(mySum)
print(add_some("AHA! ", 1, 2, 3))

# 数量可变的关键字参数
def witness(me, **who):
    print("%s saw "%me,end="")
    for k,v in who.items():
        print("{} the {} ".format(k,v),end="")
    print("flew together")
witness("Tom",阿尔托利亚="saber",英灵卫宫="archer",长江骑士="Berserker")

# 其他特性
print("OTHER ----------------------> ")
# 切片
print(list1[1:3])
print('abcde'[1:3])
# 生成器generator,类似于延迟加载
g = (x * x for x in range(10))
x = [x * x for x in range(1, 11) if x % 2 == 0]
for n in g:
    print(n,end=" ")

# join,split逆操作
names = ["tom","nancy","tony"]
print(" = ".join(names))
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
