#!/usr/bin/env python
# coding=utf-8
from pathlib import Path, PurePath
from lxml import etree

# 获取当前文件所在的目录
current_path = Path(__file__).parent
# 获取xml 文件的绝对路径
product_path = PurePath.joinpath(current_path, "products.xml")
print(product_path)
# 读取products.xml
tree = etree.parse(product_path)
print(type(tree))
# 将tree 重新转换成字符串形式的xml文档，并输出
print(str(etree.tostring(tree, encoding="utf-8"), 'utf-8'))
# 获取根节点对象
root = tree.getroot()
print(type(root))
# 输出根节点的名称
print("root:", root.tag)
# 获取根节点的所有子节点
children = root.getchildren()
print("_" * 8 + "输出产品信息" + "_" * 8)
for child in children:
    print(child.tag)
    print("product id = ", child.get('id'))
    print("child[0].name = ", child[0].text)
    print("child[1].price = ", child[1].text)

# 分析字符串形式的XML 文档
root = etree.fromstring("""
    <products>
        <product1 name="iphone"/>
        <product2 name="ipad"/>
    </products>
    """)
print("新产品")
print("root:", root.tag)
children_new = root.getchildren()
for child_new in children_new:
    print(child_new.tag, "name = ", child_new.get("name"))
