#1、显示功能界面
def info_print():
    print("请选择功能---------")
    print("1、添加学员")
    print("2、删除学员")
    print("3、修改学员")
    print("4、查询学员")
    print("5、显示所有学员")
    print("6、退出系统")
    print("-"*20)

info = [] #用来存储学员信息的列表

#添加学员的函数
def add_info():
    info_dict = {}
    new_id = input("请输入学号：")
    new_name = input("请输入姓名：")
    new_tel = input("请输入电话：")

    for i in info:
        if new_name == i["name"]:
            print("此学员已存在")
            return #return可以退出当前函数，而不执行下面的代码。

    info_dict["id"] = new_id
    info_dict["name"] = new_name
    info_dict["tel"] = new_tel
    #print(info_dict)
    info.append(info_dict)
    print(info)

def del_info():
    """删除学员"""
    #1.用户输入要删除的学员的姓名
    del_name = input("请输入需要删除的学员的姓名：")
    for i in info:
        if del_name == i["name"]:
            info.remove(i)
            print("学员已删除")
            break#如果找到重名的学员则之后的则不需要遍历了
    else:#遍历所有的学员后若没有找到需要删除的学员，则打印“学员不存在”
        print("学员不存在")
        select = input("请选择（1继续删除 2返回上级)：")
        if select == "1":
            del_info()
        else :
            info_print()

    print(info)

def modify_info():
    modify_name = input("请输入您要修改的学员的名字：")
    for i in info:
        if modify_name == i["name"]:
            new_tel = input("请输入您要修改的手机号：")
            i["tel"] = new_tel
            break
    else:
        print("您输入的学员不存在")
    print(info)

def search_info():
    search_name = input("请输入您要查询的学员的名字：")
    for i in info:
        if i['name'] == search_name:
            print("您查询的学员的信息如下：")
            print(f"名字为{i['name']},学号为{i['id']},电话为{i['tel']}") #注意引号嵌套时外面是双引号，里面是单引号。
            break
    else:
        print("您查询的学员不存在！")
    print(info)

def print_all():
    print("学号","\t","姓名","\t","电话")
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")

while True:
    info_print()

    #2、用户输入功能序号
    user_num = int(input("请输入使用序号："))


    #3、按照用户输入的序号，执行不同的功能（就是调用函数）
    if user_num == 1:
        add_info()
        #print("添加")
    elif user_num == 2:
        del_info()
       # print("删除")
    elif user_num == 3:
        modify_info()
        #print("修改")

    elif user_num == 4:
        search_info()
       # print("查询")
    elif user_num == 5:
        print_all()
        #print("显示")
    elif user_num == 6:
        exit_flag = input("确定要退出吗？ yes or no")
        if exit_flag == "yes" or"y":
            break
    else:
        print("您的输入有误！请输入1-6之间的数字。")