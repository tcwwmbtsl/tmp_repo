from fileinput import filename
from pyquery import PyQuery as pq
from pathlib import Path

html_path = Path(Path(__file__).parent, 'test.html')
doc = pq(filename=html_path)
result = doc('.item')
# 查找 class 属性值为 item 的节点的所有兄弟节点
print(result.siblings())
print('--' * 10)
# 查找 class 属性值为 item2 的兄弟节点
print(result.siblings('.item2'))
