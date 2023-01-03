from pyquery import PyQuery as pq 
import requests
import time 

# 用于下载指定的url 页面
def get_one_page(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        return None
    except Exception:
        return None 
    
def parse_one_page(html):
    doc = pq(html)
    # 提取当前 li 节点的 ul 节点
    ul = doc('.bigimg')
    liList = ul('li')
    # 对li 节点集合进行迭代，这里要注意，必须使用 items 方法返回可迭代的对象，这样每一个items 才会是PyQuery 对象
    for li in liList.items():
        # 获取当前 li 节点中的第1个 a 节点
        a = li('a:first-child')
        # 获取图书主页的URL
        href = a[0].get('href')
        # 获取图书的名称
        title = a[0].get('title')
        # 抓取 class 属性值为 search_now_price 的节点
        span = li('.search_now_price')
        # 获取价格
        price = span[0].text[1:]
        # 抓取class 属性值为 search_book_author 节点
        p = li('.search_book_author')
        # 获取图书的作者
        author = p('a:first-child').attr('title')
        # 获取图书出版日期
        date = p('span:nth-child(2)').text()[1:]
        # 获取图书出版社
        publisher = p('span:nth-child(3) > a').text()
        # 获取图书评论数
        comment_number = li('.search_comment_num').text()[:-3]
        # 获取图书简介
        detail = li('.detail').text()
        
        yield {
            'href':href,
            'title': title,
            'price':price,
            'author': author,
            'date': date,
            'publisher': publisher,
            'comment_number':comment_number,
            'detail': detail
        }
if __name__ == "__main__":
    urls = ['http://search.dangdang.com/?key=pthon&act=input&page_index={}'.format(str(i)) for i in range(1,2)]
    for url in urls:
        book_infos = parse_one_page(get_one_page(url))
        for book_info in book_infos:
            print(book_info)
            time.sleep(1)