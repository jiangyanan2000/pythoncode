
"""
1.导入模块 os
2.使用模块功能
"""
import os
#os.函数名（）
#1.文件重命名
# os.rename("1.txt","10.txt")
#2.文件删除
# os.remove("10.txt")
#3.创建文件夹mkdir(文件夹名)
# os.mkdir("aa")
#4.删除文件夹rmdir(文件夹名)
# os.rmdir("aa")
#5.获取当前目录 os.getcwd()返回当前文件所在的目录路径
print(os.getcwd())
#6.改变默认目录os.chdir(目录)
# os.chdir("aa")
# os.mkdir("bb")
#7.获取一个文件夹的所有文件，返回一个列表
files = os.listdir()
for file in files:
    print(file)
