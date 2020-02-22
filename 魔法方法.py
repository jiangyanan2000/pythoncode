"""
四、魔法方法
在python中，__xx__()的函数叫做魔法方法，指的是具有特殊功能的函数
"""
#4.1 __init__()
#4.1.1体验 __init__()
#思考 洗衣机的的宽度高度是与生俱来的属性，可不可以在生产中就赋予这些属性呢
#__init__()魔法方法的作用：初始化对象
class Washer():
    def __init__(self):
        self.width = 400
        self.height = 500
    def print_info(self):
        print(f"洗衣机的宽度是{self.width},高度是{self.height}")
w = Washer()
print(w.width)
w.print_info()

#注意：__init__()方法，在创建一个对象是被调用，不需要手动调用
# __init__(self)中的self参数，不需要开发者传入，python解释器会自动把当前的对象引用传递过去。