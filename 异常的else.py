#else是没有异常执行的代码
try:
    # print(a)
    print(1)
except Exception as result:
    print(result)
else:
    print("打印这个表示没有异常！")