#!/usr/bin/env python
# coding=utf-8


# 保护属性： _属性名
# 私有属性：__属性名
# 定义私有属性之后，python将会自动添加_类名,变相的实现了属性的隐藏，即被视为： _类名__属性名
# 当想要通过__属性名去访问属性的话，实际上访问不到的。
class Bankcard():

    def __init__(self, banknum, bankpwd, bankuser, bankmoney):
        self.bankname = "python银行"
        self.banknum = banknum
        self.bankpwd = bankpwd
        self.bankuser = bankuser
        # 私有属性
        self.__bankmoney = bankmoney

    # 私有方法
    def __login(self):
        bname = input("请输入银行账号")
        bnpwd = input("请输入账号密码")
        if bname == self.banknum and bnpwd == self.bankpwd:
            print("登录成功")
            return "ok"
        else:
            print("登录失败")

    def addmoney(self):
        r = self.__login()
        if r == "ok":
            amoney = float(input('请输入存款金额'))
            self.__bankmoney = self.__bankmoney + amoney
            print("存入", amoney, "元", "余额", self.__bankmoney, "元")


c1 = Bankcard('1001', '123', '李四', 1000)
c2 = Bankcard('1002', '456', '王五', 2000)
c1.addmoney()
