#!/usr/bin/env python
# coding=utf-8

import csv
from pathlib import Path

current_path = Path(__file__).parent
file_path = Path(current_path, 'dict_score.csv')
# csv header
fieldnames = ['id', 'stu_id', 'course_name', 'course_score']

# csv data
rows = [{
    'id': 1,
    'stu_id': 1,
    'course_name': 'English',
    'course_score': 100
}, {
    'id': 2,
    'stu_id': 1,
    'course_name': 'Math',
    'course_score': 95
}, {
    'id': 3,
    'stu_id': 2,
    'course_name': 'English',
    'course_score': 96
}]

with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# 首先，定义两个存储字段名和数据行的变量。
# 其次，调用 open() 函数以写入模式打开 CSV 文件。
# 然后，创建一个新的 DictWriter 类实例。
# 接着，调用 writeheader() 方法写入标题行。
# 最后，使用 writerows() 方法写入数据行。