#需求:尝试执行打印num，捕获异常类型nameError,如果捕获到这个异常，执行打印:有错误
try:
    print(num)
except NameError:
    print("有错误")