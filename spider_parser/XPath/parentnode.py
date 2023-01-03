#!/usr/bin/env python
# coding=utf-8


from pathlib import Path, PurePath
from lxml import etree

html_path = PurePath.joinpath(Path(__file__).parent, 'demo.html')
parser = etree.HTMLParser()
html = etree.parse(html_path, parser)
# 选取 href 属性值为 https://www.jd.com 的a 节点的父亲节点，并输出父亲节点的class 属性值 

result = html.xpath("//a[@href='https://www.jd.com']/../@class")
print("class 属性 = ", result)

# 选取 href 属性值为 https://www.jd.com 的a 节点的父亲节点，并输出父亲节点的class 属性值 

result = html.xpath("//a[@href='https://www.jd.com']/parent::*/@class")
print("class 属性值 = ", result)