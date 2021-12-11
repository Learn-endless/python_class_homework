import random
from user import User
from card import Card
# 操作类
class Atm:
    def __init__(self, alluser):  # 给Atm类一个属性，存放所有用户
        self.alluser = alluser

    def randomiCardId(self):  # 随机生成卡号
        str_data = str(random.randint(100000,999999))
        if not self.alluser.get(str):  # 判断卡号是否重复
            return str_data

    def creatUser(self):      # 开户
        name = input("请输入姓名：")
        Uid = input("请输入身份证号：")
        phone = input("请输入手机号：")
        prestMoney = float(input("请输入预存金额："))

        if prestMoney <= 0:
            print("预存金额有误，开户失败！")
            return -1
        oncePwd = input("请输入密码：")
        passPwd = input("请再次输入密码：")
        if oncePwd != passPwd:
            print("两次密码输入不一样...")
            return -1
        print("开户成功，请牢记密码：%s" % passPwd)
        cardId = self.randomiCardId()
        card = Card(cardId,oncePwd,prestMoney)
        user = User(name,Uid,phone,card)
        self.alluser[cardId] = user
        print("您的账户已开通完成，请牢记账户ID: %s" % cardId)

    def checkPwd(self, realPwd): # 检查密码的正确性
        for i in range(3):
            psd2 = input("请输入密码：")
            if realPwd == psd2:
                return True
        print("密码输错三次，系统自动退出......")
        return False

    def lockCard(self): # 给账户上锁
        inptcardId = input("请输入您的卡号：")
        user = self.alluser.get(inptcardId)
        if not user:
            print("此卡号不存在,锁定失败！")
            return -1
        if user.card.cardLock:
            print("该卡已经被锁定，无需再次锁定！")
            return -1
        if not self.checkPwd(user.card.cardPwd):
            print("密码错误...锁定失败！！")
            return -1
        user.card.cardLock = True
        print("该卡被锁定成功！")

    def searchUser(self):  # 查询操作
        inptcardId = input("请输入您的卡号：")
        user = self.alluser.get(inptcardId)
        if not user:
            print("此卡号不存在！")
            return -1
        if user.card.cardLock:
            print("该用户已经被锁定...请解卡后使用！")
            return -1
        if not self.checkPwd(user.card.cardPwd):
            print("密码错误过多,卡已经被锁定，请解卡后使用")
            user.card.cardLock = True
            return -1
        print("账户：%s 余额：%.2f" % (user.card.cardId, user.card.money))
        return user

    def getMoney(self): # 取钱
        userTF = self.searchUser()
        if userTF != -1: # 判断卡是否存在，卡的状态，输入密码的正确性
            inptMoney = float(input("请输入取款金额："))
            if inptMoney > int(userTF.card.money):
                print("输入的金额大于余额，请先查询余额！")
                return -1
            userTF.card.money = float(userTF.card.money) - inptMoney
            print("取款成功！ 账户：%s 余额：%.2f " % (userTF.card.cardId, userTF.card.money))

    def saveMoney(self): # 存钱
        userTF = self.searchUser()
        if userTF != -1: # 判断卡是否存在，卡的状态，输入密码的正确性
            if userTF.card.cardLock == False: # 确保卡的状态是解锁状态
                inptMoney = float(input("请输入要存入得金额："))
                if inptMoney < 0:
                    print("输入金额有误，请输入正确金额！")
                else:
                    userTF.card.money += inptMoney
                    print("存款成功！ 账户：%s  余额：%.2f" % (userTF.card.cardId, userTF.card.money))

    def unlockCard(self): # 账号解锁
        inptcardId = input("请输入您得卡号：")
        user = self.alluser.get(inptcardId)
        if not self.alluser.get(inptcardId):
            print("此卡号不存在，解锁失败！")
            return -1
        elif not user.card.cardLock:
            print("该卡未被锁定，无需解锁！")
            return -1
        elif not self.checkPwd(user.card.cardPwd):
            print("密码错误，解锁失败")
            return -1
        user.card.cardLock = False
        print("该卡解锁成功")
