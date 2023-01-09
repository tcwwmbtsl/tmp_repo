#!/usr/bin/env python
# coding=utf-8

from fileinput import filename
from pyquery import PyQuery as pq
from pathlib import Path
# 分析 test.html
html_path = Path(Path(__file__).parent, 'test.html')
doc = pq(filename=html_path)
# 获取 class 属性值为 item 的所有节点
result = doc('.item')
# 查找这些节点的直接父节点
print(result.parent())
print("--" * 10)
print("父节点数：", len(result.parent()))
# 查找这些节点的所有父节点
print(result.parents())
# 查找 id 属性值为 panel 的父节点
print('父节点数:', len(result.parents('#panel')))
print('节点名:', result.parents('#panel')[0].tag)
