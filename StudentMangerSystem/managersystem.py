class StudentManager(object):
    def __init__(self):
        self.student_list = []
    #一、程序入口函数
    def run(self):
        # 1.加载文件里面的学员属性
        self.load_student()
        while True:
            # 2.显示工功能菜单
            # 3.用户输入功能函数
            memu_num = int(input("请输入你需要的功能序号："))

            #4.根据用户输入的序号的不同执行不同的功能--如果用户输入1，则执行添加
            if memu_num == 1:
                #添加学员
                pass
            elif memu_num == 2:
                #删除学员
                pass
            elif memu_num ==3:
                #修改学员信息
                pass
            elif memu_num ==4:
                #查询学员信息
                pass
            elif memu_num == 5:
                #显示所有学员信息
                pass
            elif memu_num == 6:
                #保存所有学员信息
                pass
            elif memu_num == 7:
                break
    #二、系统功能函数
