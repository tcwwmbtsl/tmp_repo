#!/usr/bin/env python
# coding=utf-8

import lxml
import requests
from pathlib import Path
from bs4 import BeautifulSoup


url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
current_path = Path(__file__).parent
file_path = Path(current_path, 'sanguoyanyi.txt')
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
page_text = res.text
soup = BeautifulSoup(page_text, 'lxml')
li_list = soup.select('.book-mulu > ul > li')
fp = open(file_path,  'w', encoding='utf-8')
for li in li_list:
    title = li.a.string
    detail_url = 'https://www.shicimingju.com/' + li.a['href']
    # 对详情页进行请求，解析出章节内容
    result = requests.get(detail_url, headers=headers)
    result.encoding = 'utf-8'
    detail_page_text = result.text
    # 解析出详情页中的内容
    detail_soup = BeautifulSoup(detail_page_text, 'lxml')
    div_tag = detail_soup.find('div', class_='chapter_content')
    content = div_tag.text
    fp.write(title + ":" + "\n" + content + "\n")
    
    
    
