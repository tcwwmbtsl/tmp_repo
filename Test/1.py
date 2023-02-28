import requests
import re 
url = 'https://d3b4hd2s3d140t.cloudfront.net/putong/20230222/6W8NdNfO/500kb/hls/EyPjoxd3.ts'
       #https://d3b4hd2s3d140t.cloudfront.net/putong/20230222/6W8NdNfO/500kb/hls/7tqHuScH.ts
       #https://video.197011b.com/putong/20230222/6W8NdNfO/500kb/hls/EyPjoxd3.ts
key = '56ffd6e099dced9a'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
m3u8_url = 'https://d3b4hd2s3d140t.cloudfront.net/putong/20230222/6W8NdNfO/500kb/hls/index.m3u8'
req = requests.get(url=m3u8_url, headers=headers)
#print(req.content)
text = req.text
pat = re.compile('(.*?\.ts)')
li = re.findall(pattern=pat, string=req.text)
#print(len(li))


from Crypto.Cipher import AES 
from pathlib import Path


key = key.encode('utf-8')
# file_path = Path(r'C:\Users\86180\Downloads','EyPjoxd3 (1).ts')
# with open(file_path, 'rb') as f:
#     content = f.read()

for i in li:
    print(li.index(i))
    url = 'https://d3b4hd2s3d140t.cloudfront.net/putong/20230222/6W8NdNfO/500kb/hls/' + i
    content = requests.get(url=url, headers=headers).content
    crypto = AES.new(key, AES.MODE_CBC)
    decryption = crypto.decrypt(content)
    test_path = Path(r'C:\Users\86180\Downloads', '123.ts')
    with open(test_path, 'ab') as f:
        f.write(decryption)
