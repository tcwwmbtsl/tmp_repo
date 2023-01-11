#!/usr/bin/env python
# coding=utf-8

import requests
import pymysql 
from lxml import etree 


url = 'https://music.163.com/discover/toplist?id=3778678'
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
# print(res.status_code)
# print(res.text)
# with open('test.html', 'w', encoding='utf-8') as f:
#     f.write(res.text)
# 精卫

tree = etree.HTML(res.text)
ul = tree.xpath('//ul[@class="f-hide"]')[0]
li = ul.xpath('./li')
music_list = []
for i in li:
    song_id = i.xpath('./a/@href')[0].split('=')[1]
    name = i.xpath('./a/text()')[0]
    path = 'https://music.163.com/song?id=' + song_id
    music_list.append([name, path])
    
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1454015651@DS',charset='utf8', database='wangyiyun')
cursor = conn.cursor()
# sql_cmd = '''
#     create table music(
#         id int not null primary key,
#         name varchar(50) not null,
#         url varchar(200) not null
#     );
# '''
# cursor.execute(sql_cmd)
sql_cmd = 'insert into music(name, url) values(%s, %s);'
for i in music_list:
    print(i)
    cursor.execute(sql_cmd, i)
    conn.commit()
cursor.close()
conn.close()

