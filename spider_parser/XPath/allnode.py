#!/usr/bin/env python
# coding=utf-8

from lxml import etree
from pathlib import Path, PurePath

html_path = PurePath.joinpath(Path(__file__).parent, 'demo.html')
parser = etree.HTMLParser()
html = etree.parse(html_path, parser)
# 选取demo.html 中的所有的节点
nodes = html.xpath("//*")
print(type(nodes))
print("共 %d 个节点" % len(nodes))
# 输出所有节点的节点名
for i in nodes:
    print(i.tag, end=" ")


# 按层次输出节点，indent 是缩进
def printNodeTree(node, indent):
    print(indent + node.tag)
    indent += "  "
    children = node.getchildren()
    if len(children) > 0:
        for i in range(0, len(children)):
            printNodeTree(children[i], indent)


print()
printNodeTree(nodes[0], "")
# 选取demo.html 文件中的所有的 <a> 节点
nodes = html.xpath('//a')
print()
print("共{}个节点".format(len(nodes)))
print(nodes)
# 输出a 节点的文本内容
for i in range(0, len(nodes)):
    print(nodes[i].text, end=" ")
