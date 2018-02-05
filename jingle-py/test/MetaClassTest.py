# 类用来创建实例，而元类用来创建类，可以用于orm框架编写
# metaclass是类的模板，必须从`type`类型派生：
class ListMetaclass(type):
    # 参数分别是 当前准备创建的类的对象；类的名字；类继承的父类集合；类的方法和属性集合。
    def __new__(mcs, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        attrs['me'] = "SuperList !"
        return type.__new__(mcs, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

myList = MyList()
myList.add(1)
print(myList)
print(myList.me)

# def echo_bar(self):
#     pass
# type的另一用法，参数分别是  类的名字；类继承的父类集合；类的方法和属性集合。
# FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})

# 当写下class Foo(object)的时候，类对象Foo并不会在内存中创建：
# Python首先会看类定义中的metaclass。如果找到，就会使用它创建类对象Foo。否则，就使用type来创建。
# 元类本身还是很简单的：1）拦截类的创建；2）修改这个类；3）返回修改后的类。
