#但删除对象时，python也会默认调用__del__()方法
class Wahser():
    def __init__(self):
        self.width = 100
    def __del__(self):
        print("对象已经被删除")

w = Wahser()
del w