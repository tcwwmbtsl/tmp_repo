#!/usr/bin/env python
# coding=utf-8

"""
    使用 findall 和 finditer 查找每一次出现的位置
    findall 函数用于查询字符串中某个正则表达式模式全部的非重复出现情况,与 search 函数类似。
    与 search 和 match 函数不同的是,findall 函数总是返回一个包含搜索结果的列表。如果没有匹配到,则返回空列表
    finditer 函数在功能上与findall 函数类似，只是更节省内存。区别在于 findall 返回一个列表。finditer 返回一个迭代器
"""

import re
# 待匹配字符串
s = '12-a-abc54-a-xyz---78-A-ytr'
# 匹配以2个数字开头，结尾是3个小写字母，中间用"-a"分隔的字符串，对大小写敏感
# 下面的代码都使用了同样的模式字符串
result = re.findall(r'\d\d-a-[a-z]{3}', s)
# 运行结果：['12-a-abc', '54-a-xyz']
print(result)
# 将模式字符串加了两个分组(用圆括号括起来的部分), findall 方法也会以分组形式返回
result = re.findall(r'(\d\d)-a-([a-z]{3})', s)
# 运行结果：[('12', 'abc'), ('54', 'xyz')]
print(result)
# 忽略大小写 (最后一个参数值： re.I)
result = re.findall(r'\d\d-a-[a-z]{3}', s, re.I)
# 运行结果：['12-a-abc', '54-a-xyz', '78-A-ytr']
print(result)
# 忽略大小写并为模式添加两个分组 (最后一个参数值： re.I)
result = re.findall(r'(\d\d)-a-([a-z]{3})', s, re.I)
# 运行结果：[('12', 'abc'), ('54', 'xyz'), ('78', 'ytr')]
print(result)

# 使用finditer 并返回匹配迭代器
it = re.finditer(r'(\d\d)-a-([a-z]{3})', s, re.I)
# 对迭代器进行迭代
for result in it:
    print(result.group())
    print(result.groups())
