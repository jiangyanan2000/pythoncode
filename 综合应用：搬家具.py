"""
5.2搬家具
5.2.1需求
将小于房子剩余面积的家具摆放到房子里
5.2.2步骤分析
需求涉及两个事物：房子和家具， 故此案例涉及两个类：房子类 和家具类
·房子类
·家具类
"""
class Furniture():
    def __init__(self,name,area):
        #家具名字
        self.name = name
        #占用面积
        self.area = area

class Home():
    def __init__(self,address,area):
        self.address = address
        self.area = area
        self.free_area = area #初始化时，没有家具放入，所以剩余面积和房屋面积是一样的，在后面放入家具是才涉及到剩余面积的计算
        self.furniture= []
    def __str__(self):
        return f"房子的地理位置在{self.address},房屋面积是{self.area},剩余面积是{self.free_area},家具有{self.furniture}"

    def add_furniture(self,item):
        """容纳家具"""
        #如果家具占地面积 <= 房子剩余面积：可以搬入（家具列表添加家具名字数据并更新房子剩余面积）
        #房屋剩余面积 - 该家具的占地面积
        #否则，家具面积太大，无法放入
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print("家具太大，剩余面积不足，不能放入。")
family = Home("北京",1000)
print(family)
bed = Furniture("双人床",50)
family.add_furniture(bed)
print(family)
sofa = Furniture("沙发",10)
family.add_furniture(sofa)
print(family)
ball = Furniture("篮球场",2000)
family.add_furniture(ball)
# print(family)