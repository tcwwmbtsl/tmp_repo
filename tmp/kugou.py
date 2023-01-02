import requests
import json
from pathlib import Path

# 音乐列表
list_url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1672627750637&mid=2ae230a2b5f1d2dad186440a250ac60d&uuid=2ae230a2b5f1d2dad186440a250ac60d&dfid=3exuAM3kLAf442bQSl2Tukfs&keyword=%E5%A4%A7%E9%B1%BC&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=59f1d801736313c914eb34fd2cff9f12'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
list_resp = requests.get(url=list_url, headers=headers)
song_list = json.loads(list_resp.text[12:-2]).get('data').get('lists')
id_list = []
for i, s in enumerate(song_list):
    print(f"{i+1}-----{s.get('SongName')}----{s.get('FileHash')}----{s.get('EMixSongID')}")
    id_list.append(s.get('EMixSongID'))
print(id_list)
url = f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19103775226882264948_1672626004012&dfid=3exuAM3kLAf442bQSl2Tukfs&appid=1014&mid=2ae230a2b5f1d2dad186440a250ac60d&platid=4&encode_album_audio_id={id_list[0]}&_=1672626004013'
print(url)

data = requests.get(url, headers=headers).text
mus_url = json.loads(data[41:-2]).get('data').get('play_url')
print(mus_url)
current_path = Path(__file__).parent
song_path = Path(current_path, '大鱼.mp3')
content = requests.get(mus_url, headers=headers).content
with open(song_path, 'wb') as f:
    f.write(content)