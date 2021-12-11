# 账号实体类
class Card:
    def __init__(self, cardId, cardPwd, money, cardLock=False):
        self.cardId = cardId      # 账号ID
        self.cardPwd = cardPwd    # 账号密码
        self.money = money        # 账号金额
        self.cardLock = cardLock  # 账号状态，默认解锁
