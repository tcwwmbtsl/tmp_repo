#!/usr/bin/env python
# coding=utf-8


import requests
import re
import pathlib


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
url = 'http://www.doupoxs.com/nalanwudi/'

def getCatelogs(url):
    # 请求小说目录页面
    req = requests.get(url, headers=headers)
    result = []
    if req.status_code == 200:
        req.encoding = req.apparent_encoding
        html = req.text
    aList = re.findall('<li>.*</li>', html)
    for a in aList:
        g = re.search('href="([^"]*)"[\s]*title="([^"]*)"', a)
        if g != None:
            # 组成一个完整的URL， 每一个URL 对应一篇小说正文
            url = 'http://www.doupoxs.com' + g.group(1)
            # 得到章节的标题
            title = g.group(2)
            # 创建一个对象，用于保存标题和URL
            chapter = {'title': title, 'url':url}
            # 将该对象添加到方法返回列表中
            result.append(chapter)
    return result
            
            
def getChapterContent(chapters):
    chapter_dir = pathlib.Path(pathlib.Path(__file__).parent, 'doupo')
    if not chapter_dir.is_dir():
         chapter_dir.mkdir()
    for chapter in chapters:
        # 获取  内容
        req = requests.get(url=chapter['url'], headers=headers)
        if req.status_code == 200:
            txt_path = str(pathlib.Path(chapter_dir, chapter['title'].replace('?', ''))) + '.txt'
            with open(txt_path, 'a+', encoding='utf-8') as f:
                req.encoding = req.apparent_encoding
                contents = re.findall('<p>(.*?)</p>', req.text)
                for content in contents:
                    f.write(content + '\n')
                       
            
x = getCatelogs(url)
getChapterContent(x)