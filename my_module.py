#需求：一个函数，完成任意两个数字加法运算
def testA(x,y):
    print(x + y)

#测试信息
#__name__是系统变量，是模块的标识符，值是：如果是自身模块值是__main__,否则是当前的模块名
if __name__ == "__main__":
    testA(2,3)
    print(__name__)