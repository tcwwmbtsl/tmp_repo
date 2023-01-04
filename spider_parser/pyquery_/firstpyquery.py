#!/usr/bin/env python
# coding=utf-8

import pyquery
from pyquery import PyQuery as pq
from pathlib import Path

html = '''
<div>
    <ul>
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
    <ul>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>

'''

# 使用字符串形式将HTML 文档传入 PyQuery 对象
doc = pq(html)
# 输出 <a> 节点的href 属性值和文本内容
for a in doc('a'):
    print(a.get('href'), a.text)
# 使用 URL 形式将HTML 文档传入 PyQuery 对象
doc = pq(url='https://www.jd.com')
# 输出页面的 <title> 节点的内容
print(doc('title'))

import requests
# 抓取 HTML 代码，并将 HTML 代码传入PyQuery 对象
doc = pq(requests.get("https://www.jd.com").text)
print(doc('title'))
# 从HTML 文件将HTML 代码传入PyQuery 对象
#html_path = Path(Path(__file__).parent, 'demo.html')
doc = pq(filename='demo.html')
print(doc('head'))
