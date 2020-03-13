class MyProperty(object):
    def __get__(self, instance, owner):
        print("调用__get__",instance,owner)
    def __set__(self, instance, value):
        print("调用__set__",instance,value)
    def __delete__(self, instance):
        print("调用__del__",instance)
class C(object):
    x = MyProperty()
c = C()
c.x
c.x = 100