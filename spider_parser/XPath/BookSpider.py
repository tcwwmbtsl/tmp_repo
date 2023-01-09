#!/usr/bin/env python
# coding=utf-8
from lxml import *
from lxml import etree
import requests
import json

headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


def getOnePage(url):
    try:
        res = requests.get(url, headers=headers)
        #print(res.text)
        if res.status_code == 200:
            return res.text
        return None
    except Exception:
        return None


def parseOnePage(html):
    selector = etree.HTML(html)
    items = selector.xpath("//tr[@class='item']")
    for item in items:
        book_infos = item.xpath("td/p/text()")[0]
        yield {
            # 获取图书名称
            'name': item.xpath("td/div/a/@title")[0],
            "url": item.xpath("td/div/a/@href")[0],
            "author": book_infos.split('/')[0],
            "publisher": book_infos.split('/')[-3],
            "date": book_infos.split('/')[-2]
        }


# 将抓取到的数据保存到top250books.txt 文件中
def save(content):
    with open('top250books.txt', 'at', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


# 抓取url 对应的页面，并将页面内容保存到top250books.txt 文件中
def getTop250(url):
    html = getOnePage(url)
    for item in parseOnePage(html):
        print(item)
        save(item)


urls = [
    "https://book.douban.com/top250?start={}".format(
        str(i) for i in range(0, 250, 25))
]
for url in urls:
    getTop250(url)
