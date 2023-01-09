#!/usr/bin/env python
# coding=utf-8


import csv
from pathlib import Path

current_path = Path(__file__).parent
file_path = Path(current_path, 'score.csv')



header = ['id', 'stu_id', 'course_name', 'course_score']
data = [
    [1, 1, 'English', 100],
    [2, 1, 'Math', 95],
    [3, 2, 'English', 96]
]

with open(file_path, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerows(data)
