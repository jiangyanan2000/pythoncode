"""
三目运算符也叫三元运算符或者三元表达式
1.条件成立执行的表达式 if 条件 else条件不成立执行的表达式
"""
a = 1
b = 2
c = a if a > b else b
print(c)
# 需求：有两个变量，比较大小，如果变量1大于变量2，执行变量1-变量2 否则变量2-变量1
aa = 6
bb = 10
cc =  (aa- bb) if aa>bb else (bb-aa)
print(cc)
