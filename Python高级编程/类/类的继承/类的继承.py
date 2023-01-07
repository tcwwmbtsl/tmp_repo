#!/usr/bin/env python
# coding=utf-8

# python 中一个父类可以有多个子类
# python 中一个子类可以有多个父类
# object ： 所有类的最终父类


class animal:

    def __init__(self, color, age):
        print("animal 的初始化方法被调用")
        self.color = color
        self.age = age

    def eat(self):
        print("动物在吃")

    def run(self):
        print("动物在跑")


class Cat(animal):
    pass


class Dog(animal):
    pass


class Fish(animal):

    def swim(self):
        print('颜色', self.color, '年龄', self.age, "的鱼在游")


cat1 = Cat('白色', 3)
fish1 = Fish('花色', 4)
fish1.swim()
fish1.eat()
