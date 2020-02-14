def test1(a):
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))


b = 100
test1(b)
c = [11,22]
test1(c)
#不可变类型的id发生变化,而可变类型的id没有发生变化
