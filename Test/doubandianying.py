#!/usr/bin/env python
# coding=utf-8


import requests
import json 


url = 'https://movie.douban.com/j/chart/top_list'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "80",
    "limit": "20",
}

res = requests.get(url, headers=headers, params=param)
fp = open('./douban.json', 'w', encoding='utf-8')
json.dump(res.json(), fp=fp, ensure_ascii=False)
# print(res.json())