"""
需求分析：
参与游戏的角色
* 玩家
  手动出拳
* 电脑
  随机出拳
"""
"""
1.出拳
   玩家：手动出圈
   电脑：1.固定：剪刀；2.随机
2.判断输赢
   2.1 玩家获胜
   2.2 平局
   2.3 电脑获胜
"""
# 1.出拳
# 玩家
import random

player = int(input("请出拳： 0--表示石头；1--剪刀；2--布："))
# 电脑
computer = random.randint(0,2)
print(f"玩家出的是{player}")
print(f"电脑出的是{computer}")
# 2.判断输赢
# 3.玩家获胜
if ((player == 0) and (computer == 1) ) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print("玩家获胜，哈哈哈哈")
elif player == computer:
    print("别走，再来一局")
else:
    print("电脑赢了，电脑牛逼！！！")