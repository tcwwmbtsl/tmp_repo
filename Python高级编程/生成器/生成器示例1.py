#!/usr/bin/env python
# coding=utf-8

def intNum():
    print('开始执行')
    for i in range(5):
        yield i
        print("继续执行")


num = intNum()
print(num)