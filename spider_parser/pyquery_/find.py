from pyquery import PyQuery as  pq
from lxml import  etree
from pathlib import Path
html_path = Path(Path(__file__).parent, 'test.html')
# 分析 test.html 文件
doc = pq(filename=html_path)
# 查找所有 class 属性值为 list1 的节点，只有第一个 ul 节点满足条件
result = doc('.list1')
# 查找所有的a 节点，及子孙节点
aList = result.find('a')
print(type(aList))
for a in aList:
    # 输出每一个查找到的a节点
    print(str(etree.tostring(a, pretty_print=True, encoding='utf-8'), 'utf-8'))
print("--"*10)

# 查找所有 class 属性值为 item 的所有节点，只有第2个li节点和倒数第2个li节点满足条件
result = doc('.item')
aList = result.children('a')
for a in aList:
    # 输出每一个查找到的 a 节点
    print(str(etree.tostring(a, pretty_print=True, encoding='utf-8'), 'utf-8'))