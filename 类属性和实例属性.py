"""
类属性
设置和访问类属性
类属性就是类对象所拥有的属性，它被该类的所有实例对象所拥有
类属性可以使用类对象和实例对象访问
"""
#1.定义类，定义类属性
#2.创建对象
#3.访问类属性
class Dog(object):
    tooth = 10

xiaohei = Dog()
wangcai = Dog()
print(Dog.tooth)
print(xiaohei.tooth)
print(wangcai.tooth)
"""
类属性的优点
记录的某项数据始终保持一致时，则定义类属性
实例属性要求每个对象 为其单独开辟一份内存空间 来记录数据，而类属性为全类所共有，仅占一份内存，更加节省空间。
"""
