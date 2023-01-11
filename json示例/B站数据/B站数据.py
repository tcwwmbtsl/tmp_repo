#!/usr/bin/env python
# coding=utf-8

import requests
from pathlib import Path

url = 'https://api.bilibili.com/x/web-interface/wbi/search/type?__refresh__=true&_extra=&context=&page=1&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E7%BE%8E%E5%A5%B3&qv_id=qy7Vk2tYduoFh1J5tLnVegaMjCMGuzFN&ad_resource=5654&source_tag=3&category_id=&search_type=video&dynamic_offset=0&w_rid=0b9735625dadc9b2f3f3d839d1d5fc01&wts=1672678143'
current_path = Path(Path(__file__).parent, 'b站.csv')
res = requests.get(url)
data = res.json()
b_list = data['data']['result']

for i in b_list:
    id = i['id']
    play = i['play']
    author = i['author']
    upic = i['upic']
    with open(current_path, 'a+', encoding='utf-8') as f:
        f.write('{},{},{},{}\n'.format(id, play, author, upic))
