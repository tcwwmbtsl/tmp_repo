#!/usr/bin/env python
# coding=utf-8


def hi():
    return "hi leixin"


def soSomethingBeforeHi(func):
    print("i am dong some boring work before execute hi()")
    print(func())


# ouput:
# i am dong some boring work before execute hi()
# hi leixin
soSomethingBeforeHi(hi)
