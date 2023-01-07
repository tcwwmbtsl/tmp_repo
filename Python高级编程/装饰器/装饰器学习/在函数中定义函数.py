#!/usr/bin/env python
# coding=utf-8

# 在函数中定义函数，在Python中可以在一个函数中定义另一个函数


def hi(name='leixin'):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi function")


# output:
# now you are inside the hi() function
# now you are in the greet() function
# now you are in the welcome() function
# now you are back in the hi function
hi()

# 上面展示了无论你何时调用 hi(), greet() 和 welcome() 将会被同时调用。greet() 和 welcome() 在 hi() 函数之外是不能访问的
# output:NameError: name 'greet' is not defined
greet()
