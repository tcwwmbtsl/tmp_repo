#!/usr/bin/env python
# coding=utf-8


import requests
import json 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
data = {
   'kw':'dog' 
}

url = "https://fanyi.baidu.com/sug"
res = requests.post(url, data=data, headers=headers)
# json 方法返回的是一个对象
dic_obj = res.json()
print(dic_obj)
fp = open('.//dog.json', 'w', encoding='utf-8')
json.dump(dic_obj, fp=fp, ensure_ascii=False)