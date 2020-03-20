class A(object):
    a = 1
    def __init__(self):
        self.b = 2


aa = A()
print(aa.__dict__)
print(A.__dict__)