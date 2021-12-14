import random
while True:
    player = int(input("请出拳 石头（0） 剪刀（1） 布（2）"))
    if player == -1:
        print("退出...")
        break
    computer = random.randint(0, 2)  # 随机生成 0 1 2
    if (player == 0 and computer == 0) or (player == 1 and computer == 1) or (player == 2 and computer == 2):
        print("平局...")
    elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        print("玩家赢...")
    else:
        print("电脑赢...")

