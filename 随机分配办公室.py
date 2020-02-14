#需求：8位老师，3个办公室，将8位老师随机分配到3个办公室
"""
步骤：
1. 准备数据
   1.1 8位老师 -- 列表
   1.2 3个办公室--列表嵌套
2. 分配老师到办公室
   ***随机分配
   就是把老师的名字写入到办公室列表 -- 办公室列表追加老师名字数据
3. 验证是否分配成功
   打印办公室详细信息：每个办公室的人数和对应老师名字
"""
#1.准备数据
import random
teachers = ["A","B","C","D","E","F","G","H"]
offices = [[],[],[]]
#2.分配老师到办公室--取到每个老师放到办公室列表 --遍历老师列表数据

for name in teachers:
    num = random.randint(0,2)
    offices[num].append(name)
    # print(num)
print(offices)
#3.验证是否分配成功
i = 1
for office in offices:
    print(f"办公室{i}的人数是{len(office)}")
    for names in office:
        print(f"有{names}老师",end=" ")
        print()
    i += 1