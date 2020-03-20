from student import *
class StudentManager(object):
    def __init__(self):
        self.student_list = []
    #一、程序入口函数
    def run(self):
        # 1.加载文件里面的学员属性
        self.load_student()
        while True:
            # 2.显示工功能菜单
            self.show_menu()
            # 3.用户输入功能函数
            memu_num = int(input("请输入你需要的功能序号："))

            #4.根据用户输入的序号的不同执行不同的功能--如果用户输入1，则执行添加
            if memu_num == 1:
                #添加学员
                self.add_student()
            elif memu_num == 2:
                self.del_student()

            elif memu_num == 3:
                self.modfiy_student()

            elif memu_num == 4:
                #查询学员信息
                self.search_student()
            elif memu_num == 5:
                #显示所有学员信息
                self.show_student()
            elif memu_num == 6:
                #保存所有学员信息
                self.save_student()
            elif memu_num == 7:
                break
    #二、系统功能函数
    #2.1显示功能参菜单
    @staticmethod
    def show_menu():
        print("请选择以下功能：")
        print("1:添加学员")
        print("2:删除学员")
        print("3:修改学员信息")
        print("4:查询学员信息")
        print("5:显示所有学员信息")
        print("6:保存学员信息")
        print("7:退出系统")
    #2.2添加学员
    def add_student(self):
        name = input("请输入学员的名字：")
        gender = input("请输入学员的性别：")
        tel = input("请输入学员的电话：")
        student = Student(name,gender,tel)
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    #2.3删除学员
    def del_student(self):
        del_name = input("请输入您要删除的学员名字：")
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
        else:
            print("要删除的学员不存在！")

    #2.4修改学员信息
    def modfiy_student(self):
        modfiy_name = input("请输入要修改的学员名字：")
        for i in self.student_list:
            if modfiy_name == i.name:
                i.name = input("名字：")
                i.gender = input("性别：")
                i.tel = input("电话：")
                print(f"修改成功,姓名：{i.name}，性别：{i.gender}，电话：{i.tel}")
                break
        else:
            print("查无此人！")
    #2.5查询学员信息
    def search_student(self):
        search_name = input("请输入要查询的学员：")
        for i in self.student_list:
            if search_name == i.name:
                print(f"姓名是{i.name},性别是{i.gender},手机号是{i.tel}")
                break
        else:
            print("查无此人")

    #2.6显示学员信息
    def show_student(self):
        print("姓名\t性别\t电话")
        for i in self.student_list:
            print(f"{i.name}\t{i.gender}\t{i.tel}")
    #2.7保存学员信息
    def save_student(self):
        f = open("student.data","w")
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        f.write(str(new_list))
        f.close()
    #2.8加载学员信息
    def load_student(self):
        try:
            f = open("student.data","r")
        except:
            f = open("student.data","w")
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i["name"],i["gender"],i["tel"]) for i in new_list]
        finally:
            f.close()


