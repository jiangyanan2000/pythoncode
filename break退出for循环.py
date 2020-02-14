str1 = "itheima"
for i in str1:
    if i == "e":
        print("遇到e不打印")
        continue #break 注意体会两者的不同
    if i == "m":
        print("循环结束，拜拜啦")

        break
    print(i)
"""
注意break 和 continue 的不同
"""