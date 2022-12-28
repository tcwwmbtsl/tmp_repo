
import requests
import re
from pathlib import Path
from lxml import etree
from multiprocessing.dummy import Pool

url = 'https://www.pearvideo.com/category_1'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    
}

page_text = requests.get(url, headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
current_path = Path(Path(__file__).parent, 'lishipin')
if not Path.exists(current_path):
    Path.mkdir(current_path)
# for li in li_list:
#     detail_url = 'https://www.pearvideo.com/' + li.xpath("./div/a/@href")[0]
#     name = li.xpath("./div/a/div[2]/text()")[0]
#     #print(detail_url, name)
#     cont_id = detail_url.split('_')[1]
#     #print(cont_id)
#     url = f'https://www.pearvideo.com/videoStatus.jsp?contId={cont_id}&mrd=0.6173454071974684'
#     headers['Referer'] = detail_url
#     res = requests.get(url, headers=headers).json()
#     src_url = res['videoInfo']['videos']['srcUrl']
#     systemTime = res['systemTime']
#     rel_cont = 'cont-'+ cont_id
#     src_url = src_url.replace(systemTime, rel_cont)
#     content = requests.get(src_url, headers=headers).content
#     print(content)
#     name = name[:3] + '.mp4'
#     mp4_path = Path(current_path, name)
#     with open(mp4_path, 'wb') as f:
#         f.write(content)

def get_shipin(li):
    detail_url = 'https://www.pearvideo.com/' + li.xpath("./div/a/@href")[0]
    name = li.xpath("./div/a/div[2]/text()")[0]
    #print(detail_url, name)
    cont_id = detail_url.split('_')[1]
    #print(cont_id)
    url = f'https://www.pearvideo.com/videoStatus.jsp?contId={cont_id}&mrd=0.6173454071974684'
    headers['Referer'] = detail_url
    res = requests.get(url, headers=headers).json()
    src_url = res['videoInfo']['videos']['srcUrl']
    systemTime = res['systemTime']
    rel_cont = 'cont-'+ cont_id
    src_url = src_url.replace(systemTime, rel_cont)
    content = requests.get(src_url, headers=headers).content
    print(content)
    name = name[:3] + '.mp4'
    mp4_path = Path(current_path, name)
    with open(mp4_path, 'wb') as f:
        f.write(content)
        
        
pool = Pool(4)
pool.map(get_shipin, li_list)
    
