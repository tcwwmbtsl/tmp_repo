from pyquery import PyQuery as pq

html = '''
<div id="panel">
    <ul class="list1">
        <li class="item" value1="1234" value2 = "hello world">
            Hello
            123
            <a href="https://geekori.com"> geekori.com</a>
            World
        </li>
        <li class="item1" >
        </li>
    </ul>
    <ul class="list2">
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item"  value1="4321" value2 = "世界你好" >
            <a href="https://www.microsoft.com">微软</a>
        </li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
'''
doc = pq(html)
result = doc('.item')
# 获取节点名称
print(result[0].tag)
# 获取节点属性
print('value1:', result[0].get('value1'))
# 获取查询结果的第1个li节点的 value2 属性值
print('value2:', result.attr('value2'))
# 节点文本
print(result.text())
# 整个节点的HTML 代码
from lxml import etree

print(
    str(etree.tostring(result[0], pretty_print=True, encoding='utf-8'),
        'utf-8'))
# 节点内部的html 代码
print(result.html())
