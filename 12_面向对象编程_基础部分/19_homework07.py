import random

class RockPaperScissors:
    def __init__(self):
        self.win_count = 0  # 记录Tom赢的次数

    def play_round(self, tom_choice, computer_choice):
        """
        执行一轮游戏，判断Tom与电脑的选择，并返回结果。
        """
        # 判断平局情况
        if tom_choice == computer_choice:
            return "平"

        # 胜负逻辑：石头(0)胜剪刀(1)，剪刀(1)胜布(2)，布(2)胜石头(0)
        if (tom_choice == 0 and computer_choice == 1) or \
           (tom_choice == 1 and computer_choice == 2) or \
           (tom_choice == 2 and computer_choice == 0):
            self.win_count += 1
            return "Tom赢"
        else:
            return "电脑赢"

# 创建游戏实例
game = RockPaperScissors()

# 进行5次游戏并显示结果
for i in range(1, 6):
    tom_choice = random.choice([0, 1, 2])
    computer_choice = random.choice([0, 1, 2])
    result = game.play_round(tom_choice, computer_choice)
    print(f"第{i}次，Tom为：{tom_choice}, 电脑为：{computer_choice}, 判断为：{result}")

# 显示Tom的赢次总数
print(f"Tom的赢次总数：{game.win_count}")