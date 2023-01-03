#!/usr/bin/env python
# coding=utf-8
from pathlib import Path, PurePath
from lxml import etree
# 创建lxml.etree.HTMLParser 对象
parser = etree.HTMLParser()
print(type(parser))
# 读取并解析test.html 文件
html_path = PurePath.joinpath(Path(__file__).parent, 'test.html')
tree = etree.parse(html_path, parser)
root = tree.getroot()
# 将 HMTL 文档转换为可读格式
result = etree.tostring(root, encoding='utf-8',pretty_print=True, method="html")
print(str(result, 'utf-8'))
# 输出根节点
print('root:', root.tag)
# 输出根节点的lang 属性的值
print("lang = ", root.get('lang'))
# 输出meta节点的 charset 属性的值
print("charset = ", root[0][0].get("charset"))
# 输出 title 节点的文件
print("title = ", root[0][1].text)