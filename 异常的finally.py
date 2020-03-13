#fanlly表示的无论是否异常都要执行的代码。
try:
    f = open("test.txt","r")
except Exception as result:
    print(result)
    f = open("test.txt","w")
else:
    print("没有异常，真开心！")
finally:
    f.close()

