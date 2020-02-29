"""
故事推进:daqiu是个爱学习的好孩子，想学习更多的技术，于是在百度搜索到黑马程序员，报班学习煎饼果子技术l
所谓多继承就是一个类同时继承了多个父类
"""
class Master(object):
    def __init__(self):
        self.kongfu = "[古法煎饼果子配方]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

#创建学校类
class School(object):
    def __init__(self):
        self.kongfu = "[黑马煎饼果子配方]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")
#创建学生类
class Prentice(Master,School):
    pass

daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()
#一个类有多个父类的时候，默认使用第一个父类的同名属性和方法