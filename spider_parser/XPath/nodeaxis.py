from lxml import etree

parser = etree.HTMLParser()
text = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>XPath演示</title>
</head>
<body class="item">
<div>
    <ul class="item" >
        <li class="item1"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item2"><a href="https://www.jd.com">京东商城</a>
                            <value url="https://geekori.com"/>
                            <value url="https://www.google.com"/>
        </li>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a>
                          <a href="https://www.tmall.com/">天猫</a></li>
        <li class="item4" value="1234"><a href="https://www.microsoft.com">微软</a></li>
        <li class="item5"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
</body>
</html>
'''
html = etree.HTML(text)
# 使用ancestor 轴，用于获取所有的祖先节点。后面必须跟两个冒号(::)，然后是节点选择器
# 这里使用 * 表示匹配所有的节点

result = html.xpath("//li[1]/ancestor::*")
print(result)
for ta in result:
    print(ta.tag, end=" ")

# 使用 ancestor 轴匹配所有class属性值为 item 的祖先节点
result = html.xpath("//li[1]/ancestor::*[@class='item']")
print('*' * 10)
for value in result:
    print(value.tag, end=" ")

# 使用 attribute 轴获取第4个li节点的所有属性值
result = html.xpath("//li[4]/attribute::*")
# 输出 结果
print()
print(result)

# 使用 child 轴获取第3个 <li> 节点的所有子节点
result = html.xpath("//li[3]/child::*")
for value in result:
    print(value.get('href'), value.text, end=" ")

# 使用 descendant 轴获取第2个li节点的所有名为value 的子孙节点
print("")
result = html.xpath("//li[2]/descendant::value")
for value in result:
    print(value.get('url'), end=" ")

# 使用following 轴获取第1个<li> 节点后的所有子节点(包括子孙节点)
print()
result = html.xpath("//li[1]/following::*")
for value in result:
    print(value.tag, end=" ")

# 使用 following 轴获取第1个 <li> 节点后位置大于4的所有子节点
print()
result = html.xpath("//li[1]/following::*[position() > 4]")
for value in result:
    print(value.tag, end=" ")

# 使用following-sibling 轴获取第1个 li 节点后所有同级的节点
print()
result = html.xpath("//li[1]/following-sibling::*")
for value in result:
    print(value.tag, end=" ")
