# 用点和圆阐述继承关系
import math

class Point:
    # 类变量
    className = "Point"

    def __init__(self, x=0,y=0):
        # 实例变量
        self.x = x
        self.y = y
    def distanceFromOrigin(self):
        return math.hypot(self.x,self.y)

    #重写了这个方法就能使用+了，类似的方法还有sub等等
    def __add__(self, other):
        if not isinstance(other,Point):
            raise TypeError
        return Point(self.x + other.x,self.y + other.y)

    #重写eq方法时，默认hash方法会失效，放入set或dict时有隐患
    def __eq__(self, other):
        print("compare",self,other)
        if not isinstance(other,Point):
            return False
        return self.x==other.x and self.y==other.y

    #此方法生成的格式化字符串可用eval转化为对象。eval还能将其他格式的字符串转化为collection
    #字符串格式为： 类名（属性1，属性2，…）
    def __repr__(self):
        return "Point({},{})".format(self.x,self.y)

    #类似 Java 的 toString 方法，
    #若repr和str方法都没写，输出<__main__.Point object at 0x0029D630>
    #若有repr无str，调用repr；若有str，调用str
    def __str__(self):
        return "({},{})".format(self.x,self.y)

class Circle(Point):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.__r = 0    # 初始化半径
        self.radius = r # 给半径赋值并检查

    def area(self):
        return math.pi * self.__r ** 2

    def length(self):
        return 2 * math.pi *self.__r

    @property #使用了property修饰器，这个方法就只能被作为属性调用
    def edgeDistanceFromOrigin(self):
        return super().distanceFromOrigin() - self.__r

    @property
    def radius(self):
        return self.__r
    @radius.setter # 所有radius赋值语句将会转换成此方法，如init方法中的赋值
    def radius(self,r):
        if r<=0: raise Exception("radius must be positive number")
        self.__r = r

    def __eq__(self, other):
        return super().__eq__(other) and isinstance(other,Circle) and self.__r == other.r
    def __repr__(self):
        #可以用__r，也能用修饰器修饰过的radius，最好用后者
        return "Circle({},{},{})".format(self.x,self.y,self.radius)
    def __str__(self):
        return self.__repr__()

p1 = Point(2,6)
#!s !r !a调用p1的str/repr/ascii方法
print("str:{0!s},repr:{0!r},ascii:{0!a}".format(p1))
p2 = eval(repr(p1))
print(p2)
print(p1+p2)

print("\ncircle------------------------------>")
c1 = Circle(3,4,2)
print(c1.x)
print(c1,c1.area(),c1.length(),c1.distanceFromOrigin(),c1.edgeDistanceFromOrigin)
print(c1==p1)
#以__开头的变量不能从外部访问
# print(c1.r)
# print(c1.__r)
# 给半径赋值不是正数时报错
# c1.radius = -1
# c2 = Circle(3,4,-2)


