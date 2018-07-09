import test.ModTest as ModTest
import test.ClassTest as ClassTest

mySay = ModTest.say
mySay("hi,dog")

dog = ClassTest.Dog()
dog.name = "puppy"
dog.say()

