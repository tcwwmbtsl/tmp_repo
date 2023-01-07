#!/usr/bin/env python
# coding=utf-8

# 从函数中返回函数
# 并不需要在一个函数里去执行另一个函数，可以将其作为输出返回出来


def hi(name='leixin'):

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome function"

    if name == "leixin":
        return greet
    else:
        return welcome


a = hi()
# output:<function hi.<locals>.greet at 0x0000016A2BED48B0>
# a 指向到了 hi() 函数中的greet 函数
print(a)
# output: now you are in the greet() function
print(a())

# 解析：在 if/else 语句中，返回 greet 和 welcome ，而不是 greet 和 welcome 。因为当把小括号放在后面时，这个函数就会被执行，如果不放括号，那它就可以到处传递，并且可以赋值给别的变量而不去执行它

# output:now you are in the greet() function
print(hi()())
