#!/usr/bin/env python
# coding=utf-8

def hi(name='leixin'):
    return "hi " + name

# output: hi leixin
print(hi())

# 可以将一个函数赋值给一个变量
# 这里没有使用小括号，因为并不是在调用函数，而是将它放在 greet 这个变量里头
greet = hi 
# output: hi leixin
print(greet())

# 如果删除掉旧的hi会发生什么
# output：NameError: name 'hi' is not defined
# del hi
# print(hi())

# output: hi leixin
print(greet())