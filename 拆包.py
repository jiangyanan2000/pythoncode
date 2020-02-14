#拆包：元组

def return_num():
    return 100,200

num1,num2 = return_num()

print(num1)
print(num2)

#拆包：字典
dict1 = {"name":"tom","age":18}
a,b = dict1
print(a)
print(b)
print(dict1[a])
print(dict1[b])
