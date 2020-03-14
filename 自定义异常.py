"""
在python中，抛出自定义异常的语法为raise异常类对象
需求：密码长度不足，则报异常（用户输入密码，如果长度不足3位，则报错，即抛出自定义异常，并捕获该异常）
"""
#1.自定义异常类
class SortInputError(Exception):
    def __init__(self,length,min_len):
        self.length = length
        self.min_len = min_len
    def __str__(self):
        return f"您输入的密码长度是{self.length},不能少于{self.min_len}个字符！"
#2.抛出异常
def main():
    try:
        con = input("请输入您的密码：")
        if len(con) < 3:
            raise SortInputError(len(con),3)
    except Exception as result:
        print(result)
    else:
        print("密码输入已完成！")
#3.捕获异常
main()
# sie = SortInputError(3,4)
# print(sie)