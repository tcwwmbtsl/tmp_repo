#!/usr/bin/env python
# coding=utf-8


import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

if __name__ == "__main__":
    url = 'https://www.sogou.com/web'
    # 处理URL 携带的参数
    kw = input("enter a word:")
    param = {
        'query': kw
    }
    res = requests.get(url, params=param, headers=headers)
    page_text = res.text
    print(page_text)
    fileName = kw + ".html"
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(page_text)
    print('保存成功')