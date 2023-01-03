#!/usr/bin/env python
# coding=utf-8

from lxml import etree
from pathlib import Path, PurePath

html_path = PurePath.joinpath(Path(__file__).parent, 'demo.html')
parser = etree.HTMLParser()
html = etree.parse(html_path, parser)

# 成功选取 <a> 节点
#nodes = html.xpath("//li/a")
nodes = html.xpath("//a")
print("共{}个节点".format(len(nodes)))
print(nodes)
for i in range(0, len(nodes)):
    print(nodes[i].text, end=" ")
print("--"*20)

nodes = html.xpath("//ul//a")
print("共{}个节点".format(len(nodes)))
print(nodes)
for i in range(0, len(nodes)):
    print(nodes[i].text, end=" ")
print("--"*20)

# 无法选取 <a> 节点，因为<a> 标签不是<ul> 标签的直接子节点
nodes = html.xpath("//ul/a")
print("共{}个节点".format(len(nodes)))
print(nodes)
   
