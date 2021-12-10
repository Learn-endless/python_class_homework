import random
from user import User
from card import Card

class Atm:
    def __init__(self, alluser):  # 给Atm类一个属性，存放所有用户
        self.alluser = alluser

    def randomiCardId(self):  # 随机生成卡号
        str_data = ''+random.randint(100000,999999)
        if not self.alluser.get(str):
            return str_data

    @property
    def creatUser(self):      # 开设账户
        name = input("请输入姓名：")
        Uid = input("请输入身份证号：")
        phone = input("请输入手机号：")
        prestMoney = input("请输入预存金额：")

        if prestMoney <= 0:
            print("预存金额有误，开户失败！")
            return -1
        oncePwd = input("请输入密码：")
        passPwd = input("请再次输入密码：")
        if oncePwd != passPwd:
            print("两次密码输入不一样...")
            return -1
        print("开户成功，请牢记密码：%s" % passPwd)
        cardId = self.randomiCardId()    # 生成账户
        card = Card(cardId)
        user = User(name, Uid, phone, card)
