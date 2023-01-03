#!/usr/bin/env python
# coding=utf-8

"""
    匹配多个字符串
    要搜索多个字符串：如 biKe, car, truc
    最简单的方法是在文本模式字符串中使用择一匹配符号(|),与 逻辑或类似,只要满足任何一个,就匹配成功
"""

import re 
# 指定使用择一匹配符号的文本模式字符串
s = 'Bill|Mike|Jhon'
m = re.match(s, 'Bill')
if m is not None:
    # 运行结果：Bill
    print(m.group())
    
m = re.match(s, 'Bill:my friend')
if m is not None:
    # 运行结果：Bill
    print(m.group())

# 搜索成功
m = re.search(s, 'where is Mike')
if m is not None:
    # 运行成功：Mike
    print(m.group())
# 运行结果：<re.Match object; span=(9, 13), match='Mike'>
print(m)