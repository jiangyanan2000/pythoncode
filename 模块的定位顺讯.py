"""
当导入一个模块，python解析器对模块位置的搜索顺序是：
1、当前目录
2、如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每一个目录
3、如果都找不到，则python会查看默认路径
模块搜索路径存储在system模块sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。
·注意：
自己的文件名不要和已有模块重名，否则会导致模块功能无法使用
使用from模块名import功能的时候，如果功能名字重复，调用到的是最后定义或导入成功的功能。

"""
import random
list1 = []
for i in range(20):
    num = random.randint(1,10)
    list1.append(num)
print(list1)