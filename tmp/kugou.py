import requests

song_name = '常山来将 小魂'
url = f'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1672581391634&mid=2ae230a2b5f1d2dad186440a250ac60d&uuid=2ae230a2b5f1d2dad186440a250ac60d&dfid=3exuAM3kLAf442bQSl2Tukfs&keyword={song_name}&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=aec77de4d61ed92a53f295b861624825'
# uri = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1672581770608&mid=2ae230a2b5f1d2dad186440a250ac60d&uuid=2ae230a2b5f1d2dad186440a250ac60d&dfid=3exuAM3kLAf442bQSl2Tukfs&keyword=%E4%B8%80%E7%9C%BC%E4%B8%87%E5%B9%B4                        &page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=db02d8de6811b759816f1cd21f7a27ae'
url2 = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19109804503544324801_1672582414754&dfid=3exuAM3kLAf442bQSl2Tukfs&appid=1014&mid=2ae230a2b5f1d2dad186440a250ac60d&platid=4&encode_album_audio_id=4fvckbfe&_=1672582414755'

# res = requests.get(url)
# print(res.text)
res = requests.get(url2)
res.encoding = 'utf-8'
print(res.text)