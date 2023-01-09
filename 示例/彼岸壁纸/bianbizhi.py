#!/usr/bin/env python
# coding=utf-8

import requests
import re

url = 'http://www.netbian.com/index_2.htm'

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
print(response.text)
pattern = '<a href="/desk/29145.htm" title="(.*?) 更新时间.*?<<img src="(.*?)"'
# <a href="/desk/29145.htm" title="原创 兔年吉祥 2023年1月日历桌面壁纸 更新时间：2023-01-04" target="_blank"><img src="http://img.netbian.com/file/2022/1213/small233252tEQi81670945572.jpg" alt="原创 兔年吉祥 2023年1月日历桌面壁纸"><b>原创 兔年吉祥 2023年1月日历桌面壁纸</b></a>
li_list = re.findall(pattern, response.text)
print(li_list)