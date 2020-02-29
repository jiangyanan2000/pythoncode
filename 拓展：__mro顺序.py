class Master(object):
    def __init__(self):
        self.kongfu = "[古法煎饼果子配方]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

#创建学校类
class School(object):
    def __init__(self):
        self.kongfu1 = "[黑马煎饼果子配方]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")
#创建学生类,添加和父类同名的属性和方法
class Prentice(Master,School):
    def __init__(self):
        self.kongfu = "[独创煎饼果子配方]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()
print(Prentice.__mro__)