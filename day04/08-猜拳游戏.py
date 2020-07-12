import random

computer = random.randint(0, 2)
print('电脑输入的', computer)

#  =是赋值，==是判断
# 猜拳游戏：用户输入012，和电脑随机输入012进行判断
player = int(input('请输入 (0)剪刀 (1)石头 (2)布:'))
print('用户输入的是', player)

# input 是用来接收用户输入的数据
# 电脑应该随机的出一个数字012
# 需要使用到随机数模块 import random
# random.randint(A,B) ==>能够生成[A，B]的随机整数


if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print('恭喜你，你赢了')
elif player == computer:
    print('平局')
else:
    print('你个垃圾，输了吧')