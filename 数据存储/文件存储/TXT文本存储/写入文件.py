#!/usr/bin/env python
# coding=utf-8

from pathlib import Path

file_path = Path(Path(__file__).parent, 'test1.txt')

# 打开文件
f = open(file_path, 'w+', encoding='utf-8')
# 直接写入
# f.write('我是雷新新')
# list 写入
li_str = ['我的小宝贝', '小元宵']
f.writelines(li_str)

f.close()