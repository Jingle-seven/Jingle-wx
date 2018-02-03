# 装饰器，类似spring的AOP
import functools

def yell(func):
    @functools.wraps(func)  # 把被包装函数的文档和名字复制到包装函数
    def funcYell(*a,**ka):
        # 可以很容易地获取到原函数的参数和结果
        print("{} is running !!! args:{} {}".format(func.__name__,a,ka))
        return func(*a,**ka)
    return funcYell

# 加上这个注解后，对于此函数的调用就成了对包装函数的调用
@yell
def add(x,y):
    return x + y

# 和java注解一样，装饰器也能加参数，此处略去不表
@yell
def sub(x,y):
    return x - y

print(add(1,5))
print(sub(1,5))

