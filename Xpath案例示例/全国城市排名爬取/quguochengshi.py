#!/usr/bin/env python
# coding=utf-8


import requests
from lxml import etree 



url = 'https://www.aqistudy.cn/historydata/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers, verify=False)
res.encoding = 'utf-8'
page_text = res.text

# 数据解析
tree = etree.HTML(page_text)

hot_city_list = tree.xpath("//div[@class='bottom']/ul/li/a | //div[@class='bottom']/ul/div[2]/li/a")
for i in hot_city_list:
    print(i.text)