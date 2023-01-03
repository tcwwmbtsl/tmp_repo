#!/usr/bin/env python
# coding=utf-8

"""
   如果待匹配的字符串中,某些字符可以有多个选择,就需要使用字符集
   符号：[] 
   单个字符使用或关系时,字符集和择一匹配符效果是一样的
   如果对长度大于1的字符串使用单个字符,字符集就无能为力,只能使用择一匹配符
   如果多个字符集写在一起,相当于字符串的连接
    """

import re 

# 使用字符集，匹配成功
m = re.match('[ab][cd][ef][gh]', 'adfh')
if m is not None:
    # 运行结果: adfh
    print(m.group())

# 使用字符集，匹配成功
m = re.match('[ab][cd][ef][gh]', 'bceg')
# 运行结果：bceg
print(m.group())

# 使用字符集，匹配不成功, 因为a 和 b 是或的关系
m = re.match('[ab][cd][ef][gh]', 'abceh')
# 运行结果：None
print(m)

# 字符集和普通文本模式字符串混合使用，匹配成功，ab 相当于前缀
m = re.match('ab[cd][ef][gh]', 'abceh')
# 运行结果：abceh
print(m.group())
# 运行结果：<re.Match object; span=(0, 5), match='abceh'>
print(m)

# 使用择一匹配符，匹配成功， abcd 和 efgh 是或的关系，只要满足一个即可
m = re.match('abcd|efgh', 'efgh')
# 运行结果： efgh
print(m.group())
# 运行结果：<re.Match object; span=(0, 4), match='efgh'>
print(m)

