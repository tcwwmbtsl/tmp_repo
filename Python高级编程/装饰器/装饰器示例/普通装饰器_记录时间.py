#!/usr/bin/env python
# coding=utf-8


import time
from functools import wraps 

def recode_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"共计花费时间{end_time-start_time}")
    return wrapper

@recode_time
def my_func():
    time.sleep(3)
    print("do something  OK")
    

my_func()