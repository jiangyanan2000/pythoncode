#在python中，可以为实例属性和方法设置私有权限，即设置某个实例属性和方法不继承给子类
"""
故事：daqiu把技术传承给徒弟的同时，不想把自己的钱继承给徒弟，这个时候就要为钱这个属性设置私有权限。
设置私有属性的方法：在属性和方法名前面加双下划线
"""
class Master(object):
    def __init__(self):
        self.kongfu = "[古法煎饼果子配方]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")
class School(Master):
    def __init__(self):
        self.kongfu = "[黑马煎饼果子配方]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")
        # super(School,self).__init__()
        # super(School,self).make_cake()
        super().__init__()
        super().make_cake()
#创建学生类,添加和父类同名的属性和方法
class Prentice(School):
    def __init__(self):
        self.kongfu = "[独创煎饼果子配方]"
        # self.money = 20000
        self.__money = 20000
    def __info_print(self):
        print("这是一个私有方法。")
    def make_cake(self):
        #如果不加这个自己的初始化，kongfu的值就是上一次调用的init内的kongfu的值
        self.__init__()
        # Prentice.__init__(self) 两种方法
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
    def make_old_cake(self):
        #方法一:如果定义的类名需要修改，那么这里的类名也需要修改；代码量大，冗余
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)
        #方法二：super(当前类名,self).函数()
        # super(Prentice,self).__init__()
        # super(Prentice,self).make_cake() #在这里只能调用到Prentice类的父类，也就是School类的方法，如果想要调用Master的方法，则需要在School类中添加super方法
        #方法三：super().__init__()不带参数,同样的，若要继承更高级类的，则需要在父类添加super方法
        super().__init__()
        super().make_cake()
class Disciple(Prentice):
    pass

xiaoqiu = Disciple()
# print(xiaoqiu.__money)
xiaoqiu.__info_print()
# xiaoqiu.make_old_cake()