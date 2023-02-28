#!/usr/bin/env python
# coding=utf-8

import requests
import  base64
from Crypto.Cipher import AES 


keys = '4d975308c9eafc8f'
# key = base64.b64decode(keys)
# iv = '00000000000000000000000000000000'
# iv = bytes.fromhex(iv)

def str2hex(s):
    odata = 0;
    su =s.upper()
    for c in su:
        tmp=ord(c)
        if tmp <= ord('9') :
            odata = odata << 4
            odata += tmp - ord('0')
        elif ord('A') <= tmp <= ord('F'):
            odata = odata << 4
            odata += tmp - ord('A') + 10
    return odata

data = str2hex(keys)
print(data)

