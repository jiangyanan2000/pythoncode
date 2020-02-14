class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print(f"{self.name}正在学习{course_name}。")
    def watch_movie(self):
        if self.age < 18:
            print(f"{self.name}只能观看《熊出没》。")
        else:
            print(f"{self.name}正在观看岛国爱情大电影。")

def main():
    stu1 = Student("姜亚南",33)
    stu1.study("python程序设计")
    stu1.watch_movie()
    stu2 = Student("王大锤",13)
    stu2.study("思想品德")
    stu2.watch_movie()

if __name__ == "__main__":
    main()