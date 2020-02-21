"""
属性即是特征，比如：洗衣机的宽度、高度、重量
对象属性可以在类外面添加和获取，也能在类里面添加和获取
"""
#3.1类外面添加对象属性
class Washer():
    def wash(self):
        print("洗衣服")
haier1 = Washer()
#添加属性 对象名.属性名（） = 值
haier1.width = 400
haier1.height = 500
