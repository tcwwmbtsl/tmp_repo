#!/usr/bin/env python
# coding=utf-8

from lxml import etree
from pathlib import Path 

html_path = Path(Path(__file__).parent, 'demo.html')
parser  = etree.HTMLParser()
html = etree.parse(html_path, parser)

# 选取 href 属性值为 https://www.jd.com 或 https://geekori.com 的 <a> 节点
aList = html.xpath("//a[@href='https://www.jd.com' or @href='https://geekori.com']")
for a in aList:
    print(a.text, a.get('href'))
    
# 匹配 <li class="item4" values="1234"><a href="https://www.microsoft.com">微软</a></li>
# 选取href 属性值包含 www, 并且父节点中 value 属性值等于 1234 的 <a> 节点
print('---------------------')
aList = html.xpath('//a[contains(@href, "www") and ../@value="1234"]')
for a in aList:
    print(a.text, a.get('href'))