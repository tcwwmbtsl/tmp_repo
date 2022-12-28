#!/usr/bin/env python
# coding=utf-8


import requests
from lxml import etree
from code_platform import YdmVerify
from pathlib  import Path

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
code_jpg_path = Path(Path(__file__).parent, 'code.jpg')

page_text = requests.get(url, headers=headers).text

tree = etree.HTML(page_text)
res = tree.xpath('//*[@id="imgCode"]/@src')[0]
jpg_url = f'https://so.gushiwen.cn{res}'
print(jpg_url)
content = requests.get(jpg_url, headers=headers).content

with open(code_jpg_path, 'wb') as f:
    f.write(content)

Y = YdmVerify()
with open(code_jpg_path, 'rb') as f:
        s = f.read()
    #Y.click_verify(image=s, extra="家,炉,私")
Y.common_verify(s)

    

