#!/usr/bin/env python
# coding=utf-8

"""
    一些常用的正则表达式
"""

# Email '[0-9a-zA-Z]+@[0-9A-Za-z]+\.[a-zA-Z]{2,3}'
# IP 地址：'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# web 地址： 'https?:/{2}\w.+'

import re 
# 匹配 Email 的正则表达式
email = '[0-9a-zA-Z]+@[0-9A-Za-z]+\.[a-zA-Z]{2,3}'
result = re.findall(email, 'lining@geekori.com')
# 运行结果：['lining@geekori.com']
print(result)
result = re.findall(email, 'abcdefg@aa')
# @ 后面不是域名形式，匹配失败。运行结果：[]
print(result)
result = re.findall(email, '我的 email 是 lining@geekori.com , 不是 bill@geekori.cn, 请确认输入email 是否正确')
# 运行结果：['lining@geekori.com', 'bill@geekori.cn']
print(result)

# 匹配 IPV4 正则表达式
ipv4 = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
result = re.findall(ipv4, '这是我的IP地址: 33.12.54.34,你的IP地址是 100.32.53.12 吗')
# 运行结果是：['33.12.54.34', '100.32.53.12']
print(result)

# 匹配 URL 的正则表达式
url = 'https?:/{2}\w.+'
url1 = 'https://geekori.com'
url2 = 'ftp://geekori.com'

# 运行结果：<re.Match object; span=(0, 19), match='https://geekori.com'> 
print(re.match(url, url1))
# 运行结果：
print(re.match(url, url2))