"""
修改类属性
类属性只能通过类对象来修改，不能通过实例对象修改，如果通过实例对象来修改类属性，表示的是创建了一个实例属性
"""
class Dog(object):
    tooth = 10

# Dog.tooth = 12
# wangcai = Dog()
# xiaohei = Dog()
# print(wangcai.tooth)
# print(xiaohei.tooth)
xiaohei = Dog()
wangcai = Dog()
xiaohei.tooth = 15
print(xiaohei.tooth)
print(wangcai.tooth)
print(Dog.tooth)
