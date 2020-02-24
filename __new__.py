class demoClass:
    instances_created = 0
    def __new__(cls, *args, **kwargs):
        print("__new__():",cls,args,kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1
        return instance
    def __init__(self,attribute):
        print("__init__():",self,attribute)
        # self.attribute = attribute

test1 = demoClass("abc")
test2 = demoClass("xyz")
print(dir(test1))
# print(test1.number,test1.instances_created)
# print(test2.number,test2.instances_created)
