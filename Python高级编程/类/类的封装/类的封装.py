#!/usr/bin/env python
# coding=utf-8


#定义一个Account类
class Account:

    # 普通属性
    bank = "BOC"
    # 内部属性
    _username = "Hogwarts"
    # 私有属性
    __password = "888"


# 通过类名访问类属性
print(Account.bank)       # 将会打印 BOC
print(Account._username)  # 将会打印 Hogwarts
print(Account.__password) # 将会引发 AttributeError，打印内容：AttributeError: type object 'Account' has no attribute '__password'
print(Account.__dict__)   # 将会打印类中实际有用属性
#打印内容：{'__module__': '__main__', 'bank': 'BOC', '_username': 'Hogwarts', '_Account__password': '888', '__dict__': <attribute '__dict__' of 'Account' objects>, '__weakref__': <attribute '__weakref__' of 'Account' objects>, '__doc__': None}
#注：__dict__:python内置特殊属性，字典格式，保存类中所拥有的可写的属性

