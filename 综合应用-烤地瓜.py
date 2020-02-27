"""
5.1.2步骤分析
需求涉及一个事物：地瓜，故案例涉及一个类：地瓜
5.1.2.1定义类
·地瓜的属性
 ·被烤的时间
 ·地瓜的状态
 ·添加的调料
·地瓜的方法
 ·被烤
   用户根据意愿设定每次烤地瓜的时间
   判断地瓜被烤的总时间是在哪个区间，修改地瓜状态
 ·添加调料
   用户根据意愿设定添加的调料
   将用户添加的调料存储
·显示对象信息
"""
#代码实现
#1.定义类：初始化属性、被烤和添加调料的方法、显示对象的信息str
class SweetPotato():
    def __init__(self):
        #被烤时间
        self.cook_time = 0
        #烤的状态
        self.cook_static = "生的"
        #调料列表
        self.condiments = []
    def cook(self,time):
        """烤地瓜方法"""
        #1.先计算地瓜整体烤过的时间
        self.cook_time += time
        #2.用整体烤过的时间再判断地瓜的状态
        if 0 <= self.cook_time < 3:
            self.cook_static = "生的"
        elif 3 <= self.cook_time <5:
            self.cook_static = "半生不熟"
        elif 5 <= self.cook_time <8:
            self.cook_static = "熟了"
        elif self.cook_time >= 8:
            self.cook_static = "烤糊了"
    def add_condiments(self,condiment):
        self.condiments.append(condiment)
    def __str__(self):
        return f"这个地瓜烤了{self.cook_time}分钟,地瓜现在是{self.cook_static},调料有{self.condiments}."




#2.创建对象并调用对应的实例方法
sp = SweetPotato()
sp.cook(1)
sp.add_condiments("salt")
print(sp)
sp.cook(5)
sp.add_condiments("aginomoto")
print(sp)
sp.cook(1)
print(sp)