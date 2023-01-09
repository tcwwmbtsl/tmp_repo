#!/usr/bin/env python
# coding=utf-8

from pathlib import Path

file_path = Path(Path(__file__).parent, 'test.txt')

f = open(file_path, 'r+', encoding='utf-8')
# 方法一
# res = f.read()
# 方法二
# res = f.readline()
# res = f.readline()
# 方法三
res = f.readlines()
print(res)
# 关闭文件
f.close()
