#!/usr/bin/env python
# coding=utf-8

import requests
import json 


url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
data = {
    "cname":"", 
    "pid":"", 
    "keyword": "北京",
    "pageIndex": "1",
    "pageSize": "10"
}

res = requests.post(url, headers=headers, data=data)
fp = open('./kfc.json', 'w', encoding='utf-8')
json.dump(res.json(), fp=fp, ensure_ascii=False)
print(res.json())