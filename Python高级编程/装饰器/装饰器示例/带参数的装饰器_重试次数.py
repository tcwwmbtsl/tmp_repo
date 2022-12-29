#!/usr/bin/env python
# coding=utf-8

from functools import wraps

def retry_deco(num=3):
    def my_retry(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"重试次数为{num}")
            for i in range(num):
                func(*args, **kwargs)

        return wrapper
    return my_retry


@retry_deco(4)
def my_func():
    print(1+2)
    
my_func()