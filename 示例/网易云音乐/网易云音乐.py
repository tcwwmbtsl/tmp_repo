#!/usr/bin/env python
# coding=utf-8

import requests

url = 'https://music.163.com/discover/toplist?id=3778678'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
#     "cookie": "nts_mail_user=flfusrusr@163.com:-1:1; _iuqxldmzr_=32; _ntes_nnid=361f5b53053fa2e0b6538df7ed986c95,1662390370154; _ntes_nuid=361f5b53053fa2e0b6538df7ed986c95; WEVNSM=1.0.0; WNMCID=hiphpl.1662390370351.01.0; WM_TID=SMPxfl1FKpFAQFEBVRKEXhCpT1EQ345r; NTES_P_UTID=xw6sjoOkbknFcHmXpVZdUZKvJNndHYqV|1665744519; P_INFO=18091407402|1667737742|1|study|00&99|null&null&null#sxi&610100#10#0|&0||18091407402; NMTID=00O3MWFn3x7a-20rUzwge39HgT5lM0AAAGFBmVU4A; JSESSIONID-WYYY=K%2BVr7vCAqTHE478uafKFXGBwaBC%2Bbch%2Flg%5C0yA9HY5Mmw8OuegE%5CPPWxHqnYYYx9NKoJ27bAwPey2EA%2BFKXwNc9zelSDEuyQD8ypxnV6BK5%2FCnYv2xcXiBG9%2FuGFvDXdh7B0BVrND%2BEA0T2%2Fc2jqurhXSohjTHHbtyVSsHwYVV6Vyehk%3A1672851048791; WM_NI=rlC2LdQRY7umWXWxVDvp3duwC0worolkKG3Je1EM9kvXTuzADg%2FA1McOzMjw%2BY%2BIM%2F%2B8kRqPPx3aAqJOG43wHYSYjSibqo0DpTVMcmGTivl%2FQJIoyj4ae4lMTyzyW%2BSvc1Q%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeacf9709296819baa3bafbc8bb3d44b838e8e86d853baeafe8db241f1938a95b52af0fea7c3b92ab2b48dd3cf70938e97d8f86795889999d550b6b0fd85f87d81f0b990f165b0b585a8b242a7ef8baebc61b6889c96f94b88b9e1a2b447a191b6aee97de987e5aad025e9e8a5b3f45c94a8fd82c47b8a9189d5b27d8c879dbae959abbebf90b350b48c9aaee267858ca797ef2593968790fc62f8bfabd5ef4798a7b69ad62191aaadd2d437e2a3",
#     'accept': 'application/json, text/javascript',
#     'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'accept-encoding': 'gzip, deflate, br',
#     'content-type': 'application/x-www-form-urlencoded',
#     'origin': 'https://y.music.163.com/',
#     'referer': 'https://y.music.163.com/',
#     # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
#     # 'sec-ch-ua-mobile': '?1',
#     # 'sec-ch-ua-platform': '"Android"',
#     # 'sec-fetch-dest': 'empty',
#     # 'sec-fetch-mode': 'cors',
#     # 'sec-fetch-site': 'same-site',
# }

headers = {
    "authority":"music.163.com",
    "method":"GET",
    "path":"/discover/toplist?id=3778678",
    "scheme":"https",
    "accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "accept-encoding":"gzip, deflate, br",
    "accept-language":
    "zh-CN,zh;q=0.9",
    "cookie":
    'nts_mail_user=flfusrusr@163.com:-1:1; _iuqxldmzr_=32; _ntes_nnid=361f5b53053fa2e0b6538df7ed986c95,1662390370154; _ntes_nuid=361f5b53053fa2e0b6538df7ed986c95; "WEVNSM=1.0.0; WNMCID=hiphpl.1662390370351.01.0; WM_TID=SMPxfl1FKpFAQFEBVRKEXhCpT1EQ345r; NTES_P_UTID=xw6sjoOkbknFcHmXpVZdUZKvJNndHYqV|1665744519; P_INFO=18091407402|"1667737742|1|study|00&99|null&null&null#sxi&610100#10#0|&0||18091407402; NMTID=00O3MWFn3x7a-20rUzwge39HgT5lM0AAAGFBmVU4A; "JSESSIONID-WYYY=K%2BVr7vCAqTHE478uafKFXGBwaBC%2Bbch%2Flg%5C0yA9HY5Mmw8OuegE%5CPPWxHqnYYYx9NKoJ27bAwPey2EA%2BFKXwNc9zelSDEuyQD8ypxnV6BK5%2FCnYv2xcXiBG9%2FuGFvDXdh7B0BVr"ND%2BEA0T2%2Fc2jqurhXSohjTHHbtyVSsHwYVV6Vyehk%3A1672851048791; "WM_NI=rlC2LdQRY7umWXWxVDvp3duwC0worolkKG3Je1EM9kvXTuzADg%2FA1McOzMjw%2BY%2BIM%2F%2B8kRqPPx3aAqJOG43wHYSYjSibqo0DpTVMcmGTivl%2FQJIoyj4ae4lMTyzyW%2BSvc1Q%3D; "WM_NIKE=9ca17ae2e6ffcda170e2e6eeacf9709296819baa3bafbc8bb3d44b838e8e86d853baeafe8db241f1938a95b52af0fea7c3b92ab2b48dd3cf70938e97d8f86795889999d550b6b0fd85f87d81f0b990f"165b0b585a8b242a7ef8baebc61b6889c96f94b88b9e1a2b447a191b6aee97de987e5aad025e9e8a5b3f45c94a8fd82c47b8a9189d5b27d8c879dbae959abbebf90b350b48c9aaee267858ca797ef2593968790"fc62f8bfabd5ef4798a7b69ad62191aaadd2d437e2a3',
    "referer":"https://music.163.com/",
    "sec-ch-ua":
    '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    "sec-ch-ua-mobile":
    "?0",
    "sec-ch-ua-platform":
    "Windows",
    "sec-fetch-dest":
    "iframe",
    "sec-fetch-mode":
    "navigate",
    "sec-fetch-site":
    "same-origin",
    "upgrade-insecure-requests":
    "1",
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
print(res.status_code)
print(res.text)
# 精卫
