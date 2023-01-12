#!/usr/bin/env python
# coding=utf-8

x = lambda y: y**2

z = map(x, [i for i in range(4)])
print(z)
# print(list(z))
# for i in z:
#     print(i)
print(next(z))
