#!/usr/bin/env python
# coding=utf-8


import requests
from lxml import etree


url = "https://bj.58.com/ershoufang/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
page_text = res.text

# 数据解析
tree = etree.HTML(page_text)
list = tree.xpath("//h3[@title]/@title")
for i in list:
    print(i)