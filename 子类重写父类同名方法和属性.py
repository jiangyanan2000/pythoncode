"""
故事：daqiu掌握了师父和培训的技术后，自己潜心钻研出自己的独门配方的一套全新煎饼果子技术
"""
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
