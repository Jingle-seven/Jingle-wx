import collections


list1 = [1, 2, 3, 4, 5]
list1.append(6)
list1 +=[7]
list1.insert(0, 0)
list1.pop(2)
print("LIST ----------------------> ",list1)
print(list1[2])
# list生成式,10以内偶数的平方,全排列
list2 = [x * x for x in range(1, 11) if x % 2 == 0]
list3 = [m + n for m in 'ABC' for n in 'XYZ']
print(list2)
print(list3)
# tuple is similar to list,but it can't be changed
tuple1 = (1, 2, 3)
print(tuple1)
# namedtuple 给元组命名，类似数据类，比起一般元组可读性更好
Student = collections.namedtuple("Stu","name age clazz")
stu1 = Student("tom",14,1215423)
print(stu1.name)
print(stu1)

# dictionary
dic = {'bob': 12, 'nancy': 14, 'maggie': 'hoho'}
print("DIC ----------------------> ",dic)
print(dic['bob'])
print(dic.get('bo'))
dic.pop('bob')
print(dic)
for key in dic:
    print(key)
for value in dic.values():
    print(value)
for k, v in dic.items():
    print(k, '=', v)

# set
s1 = {1, 3, 5, 7, }
s2 = {2, 4, 6, 7}
s3 = s1 & s2
s4 = s1 | s2
print("SET ----------------------> ",s3)
print(s4)
s4.add(8)
s4.remove(3)
print(s4)