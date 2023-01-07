#!/usr/bin/env python
# coding=utf-8

from lxml import etree
from pathlib import Path

html_path = Path(Path(__file__).parent, 'demo.html')
parser = etree.HTMLParser()

text = '''
<div>
   <a href="https://geekori.com"> geekori.com</a>
   <a href="https://www.jd.com"> 京东商城</a>
   <a href="https://www.taobao.com">淘宝</a>
   <a href="https://www.microsoft.com">微软</a>
   <a href="https://www.google.com">谷歌</a>
</div>
'''

html = etree.HTML(text)
# 选择第1个 <a> 节点
a1 = html.xpath("//a[1]/text()")
print(a1)
# 选择第2个 <a> 节点
a2 = html.xpath("//a[2]/text()")
print(a2)
# 选择最后一个 <a> 节点
lasta = html.xpath('//a[last()]/text()')
print(lasta)
# 选择索引大于3的 <a> 节点
aList = html.xpath("//a[position() > 3]/text()")
print(aList)
# 选择第2个 <a> 节点和倒数第2个 <a> 节点
aList = html.xpath('//a[position() =2 or position() = last() - 1]/text()')
print(aList)
