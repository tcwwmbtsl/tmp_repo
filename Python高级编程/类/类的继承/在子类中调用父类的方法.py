#!/usr/bin/env python
# coding=utf-8

# super().方法名()
# 类名.方法名(self)
# super(要从哪一个类的上一级类开始查找,self).方法名()
# 子类调用父类的方法时，一般都是想对父类的方法进行扩展

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def driver(self):
        print('开车太好玩了,10迈,太快了')
        
class Father(Person):
    # 如果我们现在想在原有父类的方法的基础上扩展，例如我们现在需要重写一个 init 方法
    # 可以接收name, age, gender 三个属性
    def __init__(self, name, age, gender):
        # 在父类方法中已经添加了 name 和 age 我们可以直接使用
        super().__init__(name, age)
        # 在父类方法的基础上我们再添加一个子类方法独有的属性
        self.gender = gender
        
    def driver(self):
        print("我要去天安门玩")
        
    def __str__(self):
        return f"我的姓名是{self.name}, 年龄是{self.age}, 我的性别是{self.gender}"
    
class Son(Father):
    def driver(self):
        # 调用 Person的 driver
        Person.driver(self)
        
        # 从Father 类的上一级类开始查找 
        super(Father, self).driver()
        
        # 调用 Father 中的 driver
        super().driver()
        # 如果类名是当前类可以省略
        super(Son, self).driver()
        
print(Father('Jack', 28, '男'))
s1 = Son('xiaoming', 12, '男')
s1.driver()
# 子类中调用父类方法的三种方式:
# super().方法名()   # 只能调用当前类的上一级类中的方法或函数
# 类名.方法名(self)  # 所使用的类名,必须在当前类的继承关系中  这种方法可以调用不在类中的类方法，但是不能使用self作为对象出现
# super(要从哪一个类的上级类开始查询,self).方法名()  # 类名必须在继承关系内,如果类名是当前所在的类,则可以将括号内内容省略,就是第一中方式
