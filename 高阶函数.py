"""
高阶函数：把函数作为参数传入，这样的函数叫做高阶函数.
让代码更简洁了。
"""
#map()
# def sum_num(a,b,f):
#     return f(a) + f(b)
#
# result = sum_num(3.1,4.5,abs)
# print(result)

#内置高阶函数 map() reduce() filter()

list1 = [1,2,3,4,5]
def funx(x):
    return x**2
result1 = funx(100)
print(result1)
new_list = list(map(funx,list1))
print(new_list)
#reduce(func,list),其中func必须有两个参数。每次func计算的结果继续和序列的下一个元素做累计计算
import functools
list2 = [1,2,4,5,6]
def func1(a,b):
    return a + b
result2 = functools.reduce(func1,list2)
print(result2)


#filter(func,list)函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象。
list3 = [1,2,3,4,5,6,7,8,9,10]
def func2(x):
    return x % 2 == 0
result3 = filter(func2,list3)
print(list(result3))