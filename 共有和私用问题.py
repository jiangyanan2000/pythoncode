class Test:
    def __init__(self,foo):
        self.__foo = foo
    def __bar(self):
        print(self.__foo)
        print("__bar")
def main():
        test = Test("hello")
        test.__bar()
        print(test.__foo)

# def main():
#     test = Test("hello")
#     test._Test__bar()
#     #print(test._Test__foo)

if __name__ == "__main__":
    main()
#在本例中由于给方法和属性的名字前加上了“__”使其变成私有（private）而无法访问。

#但实际上我们仍然可以通过一定的规则来实现访问test._Test__bar()

