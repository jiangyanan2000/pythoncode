"""
2.2.1 定义类
·语法
class 类名（）：
     代码
     。。。。。
2.2.2 创建对象
·语法
对象名 = 类名（）
注意：类名要满足标识符命名规则，同时遵循大驼峰命名习惯
"""
# 需求：洗衣机，功能：洗衣服
"""
class 类名（）：
    代码
    
"""
# class Washer():
#     def wash(self):
#         print("能洗衣服")

# 1.定义洗衣机类

# 2.创建对象
# 对象名 = 类名（）
# haier = Washer()


# 3.验证成果
# 打印haier对象
# 使用wash功能 --实例方法、实例方法 --对象名.Wash()
# print(haier)
# haier.wash()

"""
self是指调用改函数的对象
"""
#类 洗衣机 功能 洗衣服
# class Washer():
#     def wash(self):
#         print("洗衣服")
#         print(self)
# haier = Washer()
# print(haier)
# haier.wash()
# 由于打印对象和打印self得到的内存地址是一样的，所以self指的就是调用函数的对象
#1.一个类创建多个对象；2.多个对象都调用函数的时候，self地址是否相同
class Washer():
    def wash(self):
        print("洗衣机")
        print(self)
haier1 = Washer()
haier1.wash()

haier2 = Washer()
haier2.wash()



