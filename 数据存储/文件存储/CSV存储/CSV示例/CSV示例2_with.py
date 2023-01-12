#!/usr/bin/env python
# coding=utf-8


import csv
from pathlib import Path

current_path = Path(__file__).parent
file_path = Path(current_path, 'test.csv')
with open(file_path, 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([1,2,3,4])
    