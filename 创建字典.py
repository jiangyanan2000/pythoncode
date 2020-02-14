# # {}键值对 各个键值对用逗号隔开
# #1.有数据的字典
# dict1 = {"name":"Tom","age":20,"gender":"man"}
# print(dict1)
# #2.创建空字典
# dict2 = {}
# dict3 = dict()
#
# #字典的常见操作
# #3.1 增
# dict1["id"] = 110
# print(dict1)
# #3.2 删除 clear del
# del dict1["name"]
# print(dict1)
# dict1.clear()
# print(dict1)

# 3.4.1 key查找

dict2 = {"name":"Tom","age":20,"gender":"man"}

#get() key() values() items() ; keys、values、items都返回一个可迭代对象.items()返回一个包含着元组的列表
print(dict2.get("name"))
print(dict2.get("names"))
print(dict2.get("names","lily"))
print(dict2.keys())
print(dict2.values())
print(dict2.items())
for key in dict2.keys():
    print(key)

for key,value in dict2.items(): #这个就是拆包
    print(key,value)


