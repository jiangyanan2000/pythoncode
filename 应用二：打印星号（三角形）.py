"""
需求：
*
**
***
****
*****
"""
# 分析：一行输出星星的个数和行号是相等的，每行：重复打印行号数字个星号，将打印星号的命令重复执行5次实现打印5次
j = 0 # j表示行号
while j < 5:
    # 一行星星开始
    i = 0
    while i <= j:
        #一行内星星不能换行，取消print默认结束符
        print("*",end="")
        i += 1
    # 一行星星结束：换行显示下一行
    print()
    j += 1
# row = 5
# for i in range(row):
#     for _ in range(row - i - 1):
#         print('0', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()