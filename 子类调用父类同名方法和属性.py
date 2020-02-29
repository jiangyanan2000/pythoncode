"""
故事：很多顾客都希望也能吃到古法和黑马的技术的煎饼果子
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
#创建学生类,添加和父类同名的属性和方法
class Prentice(School,Master):
    def __init__(self):
        self.kongfu = "[独创煎饼果子配方]"
    def make_cake(self):
        #如果不加这个自己的初始化，kongfu的值就是上一次调用的init内的kongfu的值
        # self.__init__()
        Prentice.__init__(self)
        print(f"运用{self.kongfu}制作煎饼果子")
#子类调用父类的同名属性和方法：把父类的同名属性和方法再次封装
    def make_master_cake(self):
        #父类名.函数()
        #再次调用初始化的原因:这里想要调用父类的同名方法和属性，熟悉在init初始化位置，所以需要再次调用init
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

daqiu = Prentice()
daqiu.make_cake()
daqiu.make_master_cake()
daqiu.make_school_cake()
daqiu.make_cake()