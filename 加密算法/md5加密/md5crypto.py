#!/usr/bin/env python
# coding=utf-8

import hashlib

text = '1454015651@DS'


def md5_en(data):
    m = hashlib.md5()
    m.update(data)
    print(m.hexdigest())


md5_en(text.encode())