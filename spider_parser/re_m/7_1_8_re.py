#!/usr/bin/env python
# coding=utf-8
"""
 ^ 符号用于匹配字符串的开始
 $ 符号用于表示匹配字符串的结束
 \b 符号用于表示单词的边界。 边界指的是单词两侧是空格或标点符号
"""

import re
# 匹配成功
m = re.search('^The', 'The end.')
print(m)
if m is not None:
    print(m.group())

# The 在匹配字符串的最后，不匹配
m = re.search('^The', 'end. The')
print(m)
if m is not None:
    print(m.group())

# 匹配成功
m = re.search('The$', 'end. The')
print(m)
if m is not None:
    print(m.group())

# 边界匹配
m = re.search(r'\bthis', "What's this?")
print(m)
if m is not None:
    print(m.group())