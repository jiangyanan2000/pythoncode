#分析：1-100的偶数和，即2+4+6+8...得到偶数的方法如下
# 偶数即是和2取余结果为0的数字，可以加入条件语句判断是否为偶数，为偶数累加
#初始值为0，增量为2
"""
1.准备累加的数字，开始为1，结束100，增量1
2.准备保存结果的变量result
3.循环加法运算，--偶数才加法运算--和2取余为0
4.输出结果
5、验证结果
"""
#方法一：
i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        #做加法运算
        result += i
    i += 1
print(result)
#方法二：计数器控制，计数器控制增量为2
"""
1.准备累加的数据
2.准备存储结果的变量
3.循环计算
4.输出结果
"""
i = 2
result = 0
while i <= 100:
    result += i
    i += 2
print(result)
