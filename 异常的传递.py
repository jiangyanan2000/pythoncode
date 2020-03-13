#异常的传递
"""
体验异常传递
需求：
1.尝试只读方式打开test.txt文件，如果文件存在则读取文件内容，文件不存在则提示用户
2.读取内容要求：尝试循环读取内容，读取过程中如果检测到用户以外终止程序，则except捕捉异常并提示用户
"""
import time
try:
    f = open("test1.txt",encoding="utf-8")
    try:
        while True:
            con = f.readline()
            if len(con) == 0 :
                break
            time.sleep(3)
            print(con)
    except:
        print("程序被意外终止了！")



except:
    print("改文件不存在！")