#!/usr/bin/env python
# coding=utf-8

from functools import wraps


class logit():
    def __init__(self, log_file='out.log'):
        self.log_file = log_file 
        
    def __call__(self, func):
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            log_string = func.__name__ + "call back"
            print(log_string)
            with open(self.log_file, 'a') as f:
                f.write(log_string)
            func()
        return wrapper_function
    
@logit()
def my_func():
    print('123')
    
my_func()
