#!/usr/bin/env python
# coding=utf-8

import re 

# 分成 3 组：(\d{3})、(\d{4}) 和 ([a-z]{2})
m = re.match('(\d{3})-(\d{4})-([a-z]{2})', '123-4567-xy')
if m is not None:
    # 运行结果：123-4567-xy
    print(m.group())
    # 运行结果：123。 为第一组的值
    print(m.group(1))
    # 运行结果：4567 。 为第二组的值 
    print(m.group(2)) 
    # 运行结果：xy 为第三组的值 
    print(m.group(3))
    # 获取每组值组成的元组
    print(m.groups())
    
# 分成 2 组 (\d{3}-\d{4}) 和 ([a-z]{2})
m = re.match('(\d{3}-\d{4})-([a-z]{2})', '123-4567-xy')
if m is not None:
    # 运行结果：123-4567-xy
    print(m.group())
    # 运行结果：123-4567 为第一组的值
    print(m.group(1))
    # 运行结果：xy 为第二组的值
    print(m.group(2))
    # 运行结果：获取每组的值组成的元组
    print(m.groups())
    
# 分成 1 组
m = re.match('\d{3}-\d{4}-([a-z]{2})', '123-4567-xy')
if m is not None:
    # 运行结果：123-4567-xy
    print(m.group())
    # 运行结果： xy
    print(m.group(1))
# 获取每组的值组成的元素
print(m.groups())   

# 未分组
m = re.match('\d{3}-\d{4}-[a-z]{2}', '123-4567-xy')
if m is not None:
    # 运行结果：123-4567-xy
    print(m.group())
    # 运行结果： xy
    print(m.groups())
