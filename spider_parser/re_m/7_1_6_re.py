#!/usr/bin/env python
# coding=utf-8

"""
    匹配一些重复的字符串，需要对重复械进行匹配使用符号
    符号：* + 
    其中： * 表示0次到n 次， + 表示一次或多次
"""

import re 

# 匹配 'a' 'b' 'c' 三个字母按顺序从左到右排列，而且这3个字母都必须至少有一个
# abc aabc abbbccc 都可以匹配
s = 'a+b+c+'
strList =['abc', 'aabc', 'bbabc', 'aabbbccxyz']
# 只有 bbabc 无法匹配
for value in strList:
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value, s))

print("*"*20)

# 匹配任意3个数字- 任意3个小写字母
# 123-abc 433-zyx 都可以匹配成功
# 下面采用了两种设置模式字符串的方式
# [a-z] 是设置字母之间或关系的简化形式，表示 a 到 z 的26个字母可以选择任意一个
# s = '\d\d\d-[a-z][a-z][a-z]
# {3} 表示让前面修饰的特殊字符 "\d" 3次，相当于\d\d\d
s = '\d{3}-[a-z]{3}'
strList = ['123-abc', '432-xyz', '1234-xyz', '1-xyzabc', '543-zyz^%ab']
for value in strList:
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print("{}不匹配{}".format(value, s))
        
print("*"*20)        
        
# 匹配以 a 到 z 的26个字母中任意一个字母作为前缀(也可以没有这个前缀), 后面是至少 1 个数字
s = '[a-z]?\d+'
strList = ['1234', 'a123', 'ab432', 'b234abc']
# 运行结果： ab432 匹配失败，因为前缀是两个字母
for value in strList:
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value, s))
        
print("*"*20) 

# 匹配一个email 
email = '\w+@(\w+\.)*\w+\.com'
emailList = ['abc@126.com', 'test@mail.geekori.com', 'test-abc@geekori.com', 'abc@geekori.com.cn']
# test-abc@geekori.com 匹配失败，因为 test 和 abc 之间有连字符
for value in emailList:
    m = re.match(email, value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value, email))
# 搜索文本中的 email  是flfusrusr@abc.com,请发邮件到这个邮箱
strValue = '搜索文本中的 email  是flfusrusr@163.com,请发邮件到这个邮箱'
m = re.search(email, strValue)
print(m)

# 规定 @ 前面部分必须是至少 1 个字母(大写或小写)和数字，不能是其他字符
email = '[a-zA-Z0-9]+@(\w+\.)*\w+\.com'
m = re.search(email, strValue)
print(m)