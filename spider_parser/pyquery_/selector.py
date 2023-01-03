from pyquery import PyQuery as pq 

html = '''
<div id="panel">
    <ul class="list1">
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
    <ul class="list2">
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>

'''

# 创建PyQuery 对象
doc = pq(html)
# 提取 id 属性值为 panel ， 并且在该节点中所有 class 属性值为 list1 的所有节点
result = doc('#panel .list1')
# 输出 result 的类型，仍然是PyQuery 对象
print(type(result))
print(result)
# 在以 result 为根的基础上，提取其中 class 属性值为 item 的所有节点
print(result('.item'))
# 提取其中第二个 a 节点的 href 属性值和文本内容
print(result('a')[1].get('href'), result('a')[1].text)
print()
# 抓取京东商城导航条链接文本
import requests
# 请求京东商城首页，并将返回的 HTML 代码传入 pq 对象
doc = pq(requests.get('https://www.jd.com').text)
# 提取第1个ul 节点
group1 = doc('#navitems-group1')
# 输出前4个链接的文本
print(group1('a')[0].text, group1('a')[1].text, group1('a')[2].text, group1('a')[3].text)
# 输出中间4个链接的文本
group2 = doc('#navitems-group2')
print(group2('a')[0].text, group2('a')[1].text, group2('a')[2].text, group2('a')[3].text)
# 输出后两个链接的文本
group3 = doc('#navitems-group3')
print(group3('a')[0].text, group3('a')[1].text)