# 管理员实体类
class Admin:
    adminU = "admin"  # 管理员账户
    adPwd = "123"  # 管理员账户密码

    # 显示欢迎界面
    def printAdminView(self):
        print("*********************************")
        print("*****  欢迎使用银行管理系统\t*****")
        print("*********************************")
        self.adminU = input("请输入管理员账户:")
        self.adPwd = input("请输入密码:")
        return self.adminOption()  # 判断管理员账户密码的正确性

    def adminOption(self):
        if self.adminU == "admin" and self.adPwd == "123":
            return self.printSysFunctionView()  # 正确调用操作菜单
        else:
            print("管理员账号或密码错误！")
            return False

    def printSysFunctionView(self):
        print("操作成功,请稍后......")
        print("************************************")
        print("****\t1.开户\t\t2.查询\t\t****")
        print("****\t3.取款\t\t4.存款\t\t****")
        print("****\t5.解锁\t\t6.锁定\t\t****")
        print("****\t显示所以账户（A/a）\t\t****")
        print("****\t退出登录（Q/q）\t\t\t****")
        print("****\t退出系统（T/t）\t\t\t****")
        print("************************************")
        return True
