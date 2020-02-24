"""
当使用print输出对象的时候，默认打印对象的内存地址。如果定义了__str__方法，那么依就会打印从在这个方法中return的数据
"""
class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def print_info(self):
        print(f"洗衣机的宽度是{self.width}")
        print(f"洗衣机的高度是{self.height}")

    def __str__(self):
        return "这是洗衣机的说明书"
haier = Washer(10,20)
print(haier)
haier.print_info()
#注意：__str__()只能返回字符串！！！！