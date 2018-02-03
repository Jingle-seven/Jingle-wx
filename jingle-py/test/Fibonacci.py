# Fibonacci斐波那契数
def fib1(n):
    if n<=1:
        return n
    else:
        return fib1(n - 2) + fib1(n - 1)

# 不使用递归效率更高
def fib2(n):
    preNum = 0
    num = 1
    for i in range(0,n):
        temp = num
        num = num + preNum
        preNum = temp
        # print(temp)
    return preNum

# 阶乘
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)



if __name__=="__main__":
    # print(fib2(1))
    for i in range(1,10):
        print(fib2(i))
        # print(factorial(i))
        # print(fib1(i))
