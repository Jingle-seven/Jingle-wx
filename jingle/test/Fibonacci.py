# Fibonacci斐波那契数
class Fib:
    # 实现了call方法的类实际上就是一个函数，可以用Fib（）直接调用
    def __call__(self,n):
        if n<=1:
            return n
        else:
            return self.__call__(n - 2) + self.__call__(n - 1)

    # 不使用递归效率更高，静态方法实际上是一般函数
    @staticmethod
    def fib2(n):
        preNum = 0
        num = 1
        for i in range(0,n):
            temp = num
            num = num + preNum
            preNum = temp
            # print(temp)
        return preNum

    # 阶乘，类方法和类绑定
    @classmethod
    def factorial(cls,n):
        if n==1:
            return 1
        else:
            return n * Fib.factorial(n-1)

    # 覆盖此方法可以用索引和切片
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            # fib2的简化形式
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L



if __name__=="__main__":
    # 用切片调用
    print(Fib()[2:10])
    # 直接调用
    print(Fib()(2))
    for i in range(1,10):
        print(Fib.fib2(i))
        print(Fib.factorial(i))
