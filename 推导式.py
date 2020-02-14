"""
推导式：列表、字典、集合  元组没有推导式它是生成器
"""
#需求 创建一个有规律的列表 0,1,2,3,4
#1.循环实现 2.推导式实现
"""
1.1创建一个空的列表
1.2用循环将数据写入
"""
# list1 = []
# i = 0
# while i <= 10:
#     list1.append(i)
#     i += 1
# print(list1)

list3 = []
for i in range(10):
    list3.append(i)
print(list3)
list2 = [x for x in range(0,11)]
print(list2)


#带 if 的推导式
list4 = [x for x in range(10) if x % 2 == 0]
print(list4)

#多个 for 实现列表推导式
list5 = [(i,j) for i in range(3) for j in range(1,4)]
print(list5)
#字典推导式
dict1 = {i:i**2 for i in range(5)}
print(dict1)
#把两个列表合并为一个字典
dict2 = {}
list6 = ["name","age","gender"]
list7 = ["tom",12,"man"]
for i in range(len(list6)):
    dict2[list6[i]] = list7[i]

print(dict2)

dict3 = {list6[i]:list7[i]for i in range(len(list6))}
print(dict3)
# 如果两个列表的长度相同，len统计任何一个列表的长度都可以，但是如果两个列表的长度不同，len统计列表长的会报错，但是如果统计少的则不会报错
counts = {"mbp":268,"hp":125,"dell":201,"lenovo":199,"acer":99}
count1 = {key:value for key,value in counts.items() if value >= 200}
print(count1)