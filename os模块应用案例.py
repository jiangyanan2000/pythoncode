"""
需求：批量修改文件名，既可以添加指定字符串，又能删除指定字符
步骤：
1、设置添加删除指定字符串的标识
2、获取指定目录的所有文件
3、将原有文件名添加/删除指定字符串，构造新名字
4.os.rename()重命名
"""
#1.获取目录下所有文件的名字
import os
files = os.listdir()
for file in files:
    # 2.构造新的文件名
    # new_name = "python_" + file
    # index = file.rfind("_")
    if "_" in file:
        new_name = file[1:]
        # 3.重命名
        os.rename(file,new_name)

