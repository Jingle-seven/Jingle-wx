
class Mammal():
    # 类变量
    className = "Mammal"
    def __init__(self,name="mammal"):
        # 实例变量
        self.name = name
    def say(self):
        print("this is a "+self.name)
    def move(self):
        print("Moving!")

class Dog(Mammal):
    def __init__(self, name="dog"):
        super().__init__(name)
        self.name = name
    def move(self):
        print("Dog running!!!")

print(Mammal.className)
# 继承
you = Dog("Labuladuo")
you.say()
you.move()

# 获取对象属性,当不存在此属性时可以设定默认值
print(getattr(you,"name"))
print(getattr(you,"age",0))

setattr(you,"name","边境牧羊犬")
you.say()
