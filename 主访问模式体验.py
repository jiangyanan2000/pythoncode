"""
测试目标
1、访问模式对文件的影响
2、访问模式对write()的影响
3、访问模式是否可以省略
"""
# r:如果文件不存在，报错;不支持写入，如果写入仍然报错。
#f = open("test1.txt","r")
# f = open("test.txt","r")
# f.write("aa")
# f.close()
# w只写:如果文件不存在则创建新的,执行写入会覆盖原有内容
# f = open("1.txt","w")
# f.write("bbb")
# f.close()


# a:追加 如果文件不存在则创建文件，在原有内容的基础上追加内容。
# f = open("2.txt","a")
# f.write("aaa")
# f.close()
f = open("1.txt")
f.close()
#访问模式省略，如果省略了访问模式默认为r（省略是在文件存在的前提下）