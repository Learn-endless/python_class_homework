# 导入π
from math import pi

# 定义一个圆的类
class Cricle:
    def __init__(self, r):
        """
        :param r: 表示圆的半径
        """
        self.r = r
    def L(self):
        ret = 2 * pi * self.r
        return ret
    def S(self):
        ret = pi * (self.r * self.r)
        return ret

per = Cricle(5)
ret = per.L()
temp = per.S()
print("%.2f" % ret)
print("%.2f" % temp)
