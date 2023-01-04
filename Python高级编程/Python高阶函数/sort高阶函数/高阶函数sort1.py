#!/usr/bin/env python
# coding=utf-8

# 忽略字母大小写进行排序
ret = sorted(['bob', 'about', 'Credit', 'Zoo'], key=lambda x: x.lower())
print(ret)

# 按照vaLue进行排序
d1 = {"a": 3, "b": 4, "c": 2, "d": 5}
print(dict(sorted(d1.items(), key=lambda x: x[1])))

# 列表里包含元组的排序
lst = [(True, 2), (False, 1, 2), (False, 2, 1), (1, 0, 2), (True, 0, 1)]
print(sorted(lst))
