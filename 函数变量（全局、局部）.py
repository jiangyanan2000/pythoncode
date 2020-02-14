a = 100
print(a)
def testA():
    print(a)

def testB(): #B函数把a的值变成200
    global a
    a = 200 #这里的a是全局变量的a还是局部变量的a呢？
    print(a)

testA()
testB()
print(a) #这里再次打印一下a，看看a的值是多少，来确定是全局变量的a还是局部变量的a