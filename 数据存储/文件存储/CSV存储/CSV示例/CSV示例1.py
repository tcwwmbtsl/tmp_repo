#!/usr/bin/env python
# coding=utf-8

import csv
from pathlib import Path

current_path = Path(__file__).parent
file_path = Path(current_path, 'test.csv')

f = open(file_path, 'w', encoding='utf-8')
writer = csv.writer(f)
row = ["1", "2", "3"]
writer.writerow(row)
f.close()