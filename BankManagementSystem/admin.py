class Admin:
    adminU = "admin"  # 管理员账户
    adpwd = "123"  # 管理员账户密码

    # 显示欢迎界面
    def printAdminView(self):
        print("*****************************")
        print("****                     ****")
        print("****  欢迎登陆银行系统   ****")
        print("****                     ****")
        print("*****************************")
        self.adminU = input("请输入管理员账户:")
        self.adpwd = input("请输入密码:")
        self.adminOption()

    def adminOption(self):
        if(self.adminU == "admin" and self.adpwd == "123"):
            self.printsysFunctionView()
        else:
            print("管理员账号或密码错误！")

    def printsysFunctionView(self):
        print("操作成功,请稍后......")
        print("****************************")
        print("****  1.开户    2.查询  ****")
        print("****  3.取款    4.存款  ****")
        print("****  5.解锁    6.锁定  ****")
        print("****  退出（Q）         ****")
        print("****************************")
