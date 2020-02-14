mystr = "hello world and itcast and itheima and python"
new_str = mystr.replace("and", "he")
# repalce() 把and换成he #** 说明repalce 函数有返回值，返回值是修改后的字符串
print(mystr)
print(new_str)
# ****调用了replace函数后，发现原有字符串的数据并没有被修改，修改后的数据是repalce函数的返回值
# ———说明字符串是不可变数据类型
# 数据是否可以分为 可变类型 和不可变类型
# split
new_str2 = mystr.split("and", 2)
print(new_str2)
#join
list1 = ["itcast","itheima","python"]
new_list =  "...".join(list1)
print(new_list)