#1、用户输入目标文件 sound.txt.mp3 用户的输入可能是五花八门，这里要有一个判断
old_name = input("请输入你要备份的文件名字：")
# print(old_name)
# print(type(old_name))
#2、规划备份文件的名字
#2.1提取后缀 找到名字中的点 名字和后缀分离 最后侧的点才是后缀的点  字符串中查找某个子串 rfind
index = old_name.rfind(".")
if index > 0:
    postfix = old_name[index:]
# print(index)
#2.2组织新名字 = 原名字 + 【备份】+ 后缀
#原名字就是字符串中的一部分子串 切片【开始;结束；步长】
# print(old_name[:index])
# print(old_name[index:])
# new_name = old_name[:index] + "[备份]" + old_name[index:]
new_name = old_name[:index] + "[备份]" + postfix
print(new_name)
#3、备份文件写入数据（数据和元文件一样）
#3.1打开原文件和备份文件
old_f = open(old_name,"rb")
new_f = open(new_name,"wb")
#如果不确定目标文件大小，循环写入，当读取出来的数据没有了终止循环
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)
old_f.close()
new_f.close()
