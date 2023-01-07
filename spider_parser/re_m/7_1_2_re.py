#!/usr/bin/env python
# coding=utf-8
"""
    使用 search 方法在一个字符串中查找模式
    参数与 match 类似
"""

import re
# 进行文本模式匹配，匹配失败，match 方法返回None
m = re.match('python', 'i love python.')
if m is not None:
    print(m.group())
# 运行结果：None
print(m)

# 进行文本模式搜索，搜索成功
m = re.search('python', 'I love python.')
if m is not None:
    # 运行结果是：python
    print(m.group())
# 运行结果：<re.Match object; span=(7, 13), match='python'>
print(m)
