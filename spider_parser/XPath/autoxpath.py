#!/usr/bin/env python
# coding=utf-8
import requests 
from lxml import etree 

# 抓取京东商城首页的HTML 代码
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
r = requests.get("https://wwww.jd.com", headers=headers)
print(r.encoding)
print(r.apparent_encoding)
#print(html)
parser = etree.HTMLParser()
html = etree.HTML(r.text.encode(r.encoding))
# 提取第一个导航栏的内容
nodes = html.xpath("//*[@id='navitems-group1']//a/text()")
for i in nodes:
    print(i)
    
    
#//*[@id="navitems-group1"]/li[1]/a