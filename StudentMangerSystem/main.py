#1.导入信息关系系统模块
from managersystem import *
#2.启动管理系统
#保证是当前文件运行才启动管理系统
if __name__ == "__main__":
    student_manager = StudentManager()
    student_manager.run()
