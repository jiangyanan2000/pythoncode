"""
思考：一个类可以创建多个实例对象，如何对不同的对象设置不同的初始化属性呢?
答:传参数
"""
#1.定义类：带参数的init：宽度和高度；实例方法：调用实例属性
class Washer():
    def __init__(self,width,height):#这个时候实例化的时候就必须带参数了，否则会报错。
        self.width = width
        self.height = height
    def print_info(self):
        print(f"洗衣机的宽度是{self.width}")
        print(f"洗衣机的高度是{self.height}")
#2.创建对象，创建多个属性且属性值不同；调用实例方法
haier1 = Washer(10,20)
haier1.print_info()

haier2 = Washer(30,40)
haier2.print_info()

