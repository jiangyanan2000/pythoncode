"""
静态方法
静态方法的特点
需要通过装饰器@staicmethod来进行修饰，静态方法既不需要传递类对象也不需要传递实例对象
静态方法也能通过类对象和实例对象去访问
静态方法使用场景
当方法中既不需要使用实例对象（如实例属性、实例方法）也不需要使用类对象（如类属性、类方法、创建实例等）时，定义静态方法
取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
"""

class Dog(object):
    @staticmethod
    def info_print():
        print("这是一个狗类，用于创建狗实例...")
wangcai = Dog()
wangcai.info_print()
Dog.info_print()
