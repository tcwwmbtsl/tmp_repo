#!/usr/bin/env python
# coding=utf-8


# 类的声明
class Human():
    # 定义属性
    message = '这是类属性'
    
    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('这是构造方法')
        
    # 实例方法
    def study(self, course):
        print(f"正在学习{course}")
        
    # 类方法
    # 使用类方法装饰器,定义类时会自动添加 cls 参数
    @classmethod
    def born(cls):
        print("这是类方法")
        cls.population += 1
        
    @staticmethod
    def grow_up():
        print('这是静态方法')

        
        

        
    
# 通过类访问类属性
print(Human.message)

# 实例化对象
person = Human('王明', 30)
# 通过实例访问类属性
print(person.message)
# 通过实例访问实例属性
print(person.name)
print(person.age)
# 通过实例访问实例方法
person.study('python')
# 通过类名访问类方法
# Human.born()
# 通过类名访问静态方法
Human.grow_up()


