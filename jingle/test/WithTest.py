
class NumContextManagers:
    def __init__(self):
        self.num = int()
    def __enter__(self):
        print("初始化…")
        self.num = 1
        return self
    def __exit__(self, type, value, trace):
        print("处理异常和清理现场…")
        self.num = 0
    def doSomething(self):
        return 10/self.num

# 一个实现了enter和exit方法的上下文管理器被赋值到num
with NumContextManagers() as num:
    print(num.doSomething())
# with中的内容正常或者异常结束后，exit方法会被调用，类似java7的try-with-resource