#!/usr/bin/env python
# coding=utf-8

from pathlib import Path, PurePath
from lxml import etree

html_path = PurePath.joinpath(Path(__file__).parent, 'demo.html')
parser = etree.HTMLParser()
html = etree.parse(html_path, parser)

# 选取所有href 属性值为 https://geekori.com 的 <a> 节点

nodes = html.xpath("//a[@href='https://geekori.com']")
print("共{}个节点".format(len(nodes)))
print(nodes[0].text)

# 选取所有 href 属性值包含 www 的 <a>节点
nodes = html.xpath("//a[contains(@href, 'www')]")
print("共{}个节点".format(len(nodes)))
for i in range(0, len(nodes)):
    print(nodes[i].text)

urls = html.xpath("//a[contains(@href, 'www')]/@href")
for i in range(0, len(urls)):
    print(urls[i])
