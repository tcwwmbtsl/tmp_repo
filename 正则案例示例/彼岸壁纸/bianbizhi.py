#!/usr/bin/env python
# coding=utf-8

import requests
from pathlib import Path
import re

url = 'http://www.netbian.com/index_2.htm'

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
pattern = '<a href=".*?" title="(.*?)".*?<img src="(.*?)"'
# <a href="/desk/29145.htm" title="原创 兔年吉祥 2023年1月日历桌面壁纸 更新时间：2023-01-04" target="_blank"><img src="http://img.netbian.com/file/2022/1213/small233252tEQi81670945572.jpg" alt="原创 兔年吉祥 2023年1月日历桌面壁纸"><b>原创 兔年吉祥 2023年1月日历桌面壁纸</b></a>
li_list = re.findall(pattern, response.text)
print(len(li_list))
current_path = Path(__file__).parent 
dir_path = Path(current_path, 'pic')
if not Path.is_dir(dir_path):
    Path.mkdir(dir_path)

for title, url in li_list:
    file_path = Path(dir_path, title.replace(' ', '')[0:5]+'.jpg')

    content = requests.get(url, headers=headers).content
    with open(file_path, 'wb') as f:
        f.write(content)