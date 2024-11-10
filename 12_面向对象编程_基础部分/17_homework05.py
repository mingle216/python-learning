# @Version  : 1.0
# @Author   : mmh
# @File     : 13_homework01.py
# @Time     : 2024/11/8 16:23
class Music:
    def __init__(self, name, times):
        self.name = name
        self.times = times

    def play(self):
        print(f"音乐名 {self.name} 正在播放中.... 时长为{self.times}分钟")

    def get_info(self):
        return f"音乐名 {self.name}，播放时长 {self.times}分钟"


m = Music("青花瓷",4)
print(m.get_info())
m.play()
