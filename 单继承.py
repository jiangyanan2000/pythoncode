"""
故事主线：一个煎饼果子老师傅，在煎饼果子界摸爬滚打多年，研发了一套精湛的摊煎饼果子技术。师父要把这套技术传授给他的唯一的最得意的徒弟。
分析:徒弟是不是要继承师父的所有技术？
"""
#1师父类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = "[古法煎饼果子配方]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

class Prentice(Master):
    pass
#3.用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()