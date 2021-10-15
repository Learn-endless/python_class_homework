class KYRC:
    def __init__(self):
        self.zt = '生的'    # 烤羊肉串的默认状态
        self.cookie_time = 0  # 统计烤羊肉串的总时间

    def cookit(self, cookie_time):
        self.cookie_time += cookie_time
        if self.cookie_time >= 0 and cookie_time <= 3:
            self.zt = '半生不熟...'
        elif self.cookie_time > 3 and cookie_time <= 6:
            self.zt = '刚刚好...'
        else:
            self.zt = '烤糊了...'

    def __str__(self):
        """
        打印对象的时候，默认执行此方法
        :return: 必须要有字符串类型的返回值。
        """
        temp = '肉串的状态：{}'.format(self.zt)
        return temp

kyrc = KYRC()
kyrc.cookit(1)
print(kyrc)
kyrc.cookit(4)
print(kyrc)

# class Func:
#     def __str__(self):
#         """
#         打印对象的时候，默认执行此方法
#         :return: 必须要有字符串类型的返回值。
#         """
#         temp = '肉串的状态：半生不熟'
#         return temp
# temp = Func()
# print(temp)
