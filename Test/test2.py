import requests
import re 
from pathlib import Path

currrent_path = Path(__file__).parent
dir_path = Path(currrent_path, 'testss')
if not Path.is_dir(dir_path):
    Path.mkdir(dir_path)
url = 'https://www.acfun.cn/v/ac33096804'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# response = requests.get(url, headers=headers)
# print(response.encoding)
# print(response.apparent_encoding)
# print(response.text)
# print(response.status_code)

m3u8_url = 'https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/b3779578b11c1d3b-6a5ccc67e4d2f04066d19f83e32b6dfd-hls_720p_hevc_1.m3u8?pkey=ABBoPvmcVVY-3aEdZaIw_r0EGOSr15Vy9OeEKFyEhOsiEXhVUcGW3j0ZIxxPhWjvtweJ07LqSHixBmkAnn7Q0QeT4fA7sr4QVnMuHv8P2fQqNYYk9ss06OdXTaKA7LnfUmpn2V2-cymgnX9GzIH1xqPSlWi3vMnAvQIyVO77_7Kz7EFgicFMSeT8gnmCIYHOoEm73-5xMYu60CyXMgJN4WeaAqffxgVZnvFw3uIk4mI9Lp3UaKsM-rWTVaDqBv3mgFk&safety_id=AALT3iRhle63iDs6CniKw4JU'
response_m3u8 = requests.get(m3u8_url, headers=headers)
response_data = response_m3u8.text
m3u8_data = re.sub('#E.*', '', response_data).split()
#m3u8_data1 =re.findall('\n(.*?)\n', response_data)
print(m3u8_data)
for i in m3u8_data:
    ts_url = 'https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/'+i
    ts_content = requests.get(ts_url, headers=headers).content
    #ts_name = i.split('.')[1] + '.mp4'
    ts_name = 'test.mp4'
    ts_path = Path(dir_path, ts_name)
    with open(ts_path, 'ab') as f:
        f.write(ts_content)
#print(m3u8_data1)
#print(response_m3u8.text)

data = requests.get(url='https://video.197011b.com/putong/20230202/ODnwYfRi/500kb/hls/GCvcY2Dv.ts', headers=headers, verify=False).content
name = '12.mp4'
tmp_path = Path(dir_path, name)
with open(tmp_path, 'wb')as f:
    f.write(data)
