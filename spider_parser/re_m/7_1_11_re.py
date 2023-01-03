#!/usr/bin/env python
# coding=utf-8

"""
    split 函数的使用
"""
import re 
result = re.split(';', 'Bill;Mike;John')
# 运行结果：['Bill', 'Mike', 'John']
print(result)

# 至少用一个逗号(,), 分号(;), 点(.)和空白符(\s)分隔字符串
result = re.split('[,;.\s]', 'a,b,,d,d;x   c;d. e')
# 运行结果：['a', 'b', '', 'd', 'd', 'x', '', '', 'c', 'd', '', 'e']
print(result)
# 用以 3 个小写字母开头，紧接着一个连字符(-), 并以2个数字结尾的字符串作为分隔符对字符串进行分隔
result = re.split('[a-z]{3}-[0-9]{2}', 'testabc-4312productxyz-43abill')
# 运行结果：'test', '12product', 'abill']
print(result)

# 使用 maxsplit 参数限定分隔的次数，这里限定为一次，也就是只分隔一次
result = re.split('[a-z]{3}-[0-9]{2}', 'testabc-4312productxyz-43abill', maxsplit=1)
# 运行结果：['test', '12productxyz-43abill']
print(result)