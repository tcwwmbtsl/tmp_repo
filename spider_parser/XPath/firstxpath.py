#!/usr/bin/env python
# coding=utf-8
from pathlib import Path, PurePath
from lxml import etree
parser = etree.HTMLParser()
html_path = PurePath.joinpath(Path(__file__).parent, "xpath_test.html")
tree = etree.parse(html_path, parser)
# 使用 XPath 定位title 节点，返回一个节点集合
titles = tree.xpath('/html/head/title')
if len(titles) > 0:
    print(titles[0].text)
    
# 定义一段HTML 代码
html = '''
<div>
    <ul>
        <li class="item1"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item2"><a href="https://www.jd.com"> 京东商城</a></li>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
    </ul>
</div>
'''
# 分析 HTML 代码
tree = etree.HTML(html)
# 使用 XPath 定位class 属性值为 items2 的<li>节点
aTags = tree.xpath("//li[@class='item2']")
if len(aTags) > 0:
    # 得到该 <li> 节点中 <a> 节点的 href 属性值和文本
    print(aTags[0][0].get('href'),aTags[0][0].text)