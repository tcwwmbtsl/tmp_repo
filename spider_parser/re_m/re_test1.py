#!/usr/bin/env python
# coding=utf-8
"""
本例演示如何利用match 和 group 方法完成字符串的模式匹配，并输出匹配结果
"""

# 导入 re 模块
import re
# 进行文本模式匹配，匹配成功
m = re.match('hello', 'hello')
if m is not None:
    # 运行结果： hello
    print(m.group())
# 输出 m 的类名，运行结果 Match
print(m.__class__.__name__)

# 进行文本模式匹配，匹配失败，m 为 None
m = re.match('hello', 'world')
if m is not None:
    print(m.group())
# 运行结果为 None
print(m)

# 只要模式从字符串起始位置开始，也可以匹配成功
m = re.match('hello', 'hello world')
if m is not None:
    # 运行结果：hello
    print(m.group())
# 运行结果：<re.Match object; span=(0, 5), match='hello'>
print(m)
