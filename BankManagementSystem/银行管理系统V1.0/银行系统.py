import time
from admin import Admin
from atm import Atm


class HomePage:
    def __init__(self):
        self.allUserD = {} # 用来存放用户数据
        self.atm = Atm(self.allUserD) # 创建了一个Atm对象
        self.admin = Admin()          # 创建了一个Admin对象

    def saveUser(self):
        # 更新用户数据
        self.allUserD.update(self.atm.alluser)
        print("数据保存成功")

    def main(self):
        while True: # 循环输入管理员账户，知道输入正确为止
            ret = self.admin.printAdminView()  # 执行菜单方法，并判断管理员账户是否输入正确
            while ret:
                option = input("请输入您得操作：")
                if option not in ("1", "2", "3", "4", "5", "6", "Q", "q", "A", "a", "t", "T"):  # 不在选项内，则进行下一次循环
                    print("输入操作项有误，请仔细确认！")
                    time.sleep(2)
                    continue
                if option == "1":  # 开户操作
                    self.atm.creatUser()
                elif option == "2": # 查询操作
                    self.atm.searchUser()
                elif option == "3": # 取钱操作
                    self.atm.getMoney()
                elif option == "4": # 存钱操作
                    self.atm.saveMoney()
                elif option == "5": # 账户解锁
                    self.atm.unlockCard()
                elif option == "6": # 账户上锁
                    self.atm.lockCard()
                elif option == "Q" or option == "q": # 退出到登录菜单
                    self.saveUser()
                    print("退出登录》》》")
                    break
                elif option == "t" or option == "T": # 退出系统
                    print("退出系统......")
                    return 0;
                elif option == "A" or option == "a": # 显示所有用户
                    self.saveUser()  # 先更新用户数据，然后显示
                    for i in self.allUserD:
                        ret = "未锁定"
                        if self.allUserD[i].card.cardLock:
                            ret = "锁定"
                        print("账号：{0}\t手机号：{1}\t身份证号：{2}\t账号状态：{3}"
                              .format(i, self.allUserD[i].phone, self.allUserD[i].id, ret))


homePage = HomePage()
homePage.main()
