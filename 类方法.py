"""
类方法的特点
需要用装饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数
类方法使用场景
当方法中 需要使用类对象（如访问私有类属性）时，定义类方法
类方法一般和类属性配合使用
"""
#1.定义类 类里有 私有类属性 定义类方法，来获取这个私有属性
class Dog(object):
    __tooth = 100
    @classmethod
    def get_tooth(cls):
        return cls.__tooth

#2.创建对象，调用类方法

xiaohei = Dog()
result = xiaohei.get_tooth()
print(Dog.get_tooth())
# print(result)