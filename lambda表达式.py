#lambda的应用场景，就是为了简化代码
"""
lambda 参数列表：表达式
lambda表达式的参数可有可无，函数的参数在lambda表达式中完全适用
lambda表达式能接受任何数量的参数但只能返回一个表达式的值
"""

#快速入门
# def fn1():
#     return 200
#
# print(fn1)
# print(fn1())
# fn2 = lambda: 100
# print(fn2)
# print(fn2())

def add(a,b):
    return a + b

f1 = add(1,2)
print(f1)

f2 = lambda a,b :a+b
print(f2(4,5))

f3 = lambda **kwargs:kwargs
print(f3(name = "小明",age = 10,tel = 110))
