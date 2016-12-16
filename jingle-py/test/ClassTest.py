
class Mammal():
    def __init__(self,name="mammal"):
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


you = Dog("Labuladuo")
you.say()
you.move()
