#!/usr/bin/env python
# coding=utf-8
"""
    匹配任何单个字符
    正则中最长用的是匹配一类字符, 而不是一个。需要使用特殊字符来表示一类字符串
    符号： .
    转义字符：\
"""

import re

# 使用了 . 符号的文本模式字符串
s = '.ind'
# 匹配成功
m = re.match(s, 'bind')
if m is not None:
    # 运行结果： bind
    print(m.group())
m = re.match(s, 'binding')
# 运行结果：<re.Match object; span=(0, 4), match='bind'>
print(m)
m = re.match(s, 'bin')
# 运行结果：None
print(m)

# 匹配成功
m = re.search(s, '<bind>')
if m is not None:
    # 运行结果：bind
    print(m.group())
# 运行结果：<re.Match object; span=(1, 5), match='bind'>
print(m)

# 使用点(.) 符号的文本模式字符串
s1 = '3.14'
# 使用转义字符将点(.) 变成真正的点字符
s2 = '3\.14'
# 匹配成功，因为.字符同样也是一个字符
m = re.match(s1, '3.14')
# 运行结果：<re.Match object; span=(0, 4), match='3.14'>
print(m)

# 匹配成功，3和14之间可以是任意字符
m = re.match(s1, '3314')
# 运行结果：<re.Match object; span=(0, 4), match='3314'>
print(m)

m = re.match(s2, '3.14')
# 匹配成功：运行结果：<re.Match object; span=(0, 4), match='3.14'>
print(m)

m = re.match(s2, '3314')
# 匹配失败：运行结果：None
print(m)
