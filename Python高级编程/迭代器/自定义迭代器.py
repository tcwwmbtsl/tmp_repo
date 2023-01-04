#!/usr/bin/env python
# coding=utf-8

from collections.abc import Iterable, Iterator


# 自定义类实现迭代器
class SelfListIterable:

    def __init__(self):
        self.ls = []
        self.current = 0

    def add(self, ele):
        self.ls.append(ele)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.ls):
            ele = self.ls[self.current]
            self.current += 1
            return ele
        else:
            raise StopIteration


# 实例化一个对象
mylist = SelfListIterable()
mylist.add(23)
mylist.add(45)

# 注：在Python3.10 版本中移除了 from collections import Iterable,Iterator 改为 from collections.abc import Iterable,Iterator

print("mylist是否是迭代器: %s" % (isinstance(mylist, Iterator)))
print('mylist 是否是可迭代对象：%s' % (isinstance(mylist, Iterable)))
