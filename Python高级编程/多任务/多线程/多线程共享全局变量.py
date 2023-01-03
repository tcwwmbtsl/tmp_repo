#!/usr/bin/env python
# coding=utf-8

import threading
import time

g_num = 100
def test():
    global g_num 
    g_num +=1
    print("test1", g_num)
    
def test2():
    print("test2", g_num)
    
def main():
    t1 = threading.Thread(target=test)
    t2 = threading.Thread(target=test2)
    t1.start()
    time.sleep(1)
    t2.start()

if __name__ == "__main__":
    main()