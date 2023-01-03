#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Queue
import multiprocessing

def download(p):
    lst = [11, 22, 33, 44]
    for item in lst:
        p.put(item)
    print("数据已经下载成功...")

def savedata(p):
    lst = []
    while True:
        data = p.get()
        lst.append(data)
        if p.empty():
            break 
    print(lst)
    
def main():
    p1 = Queue()
    t1 = multiprocessing.Process(target=download, args=(p1,))
    t2 = multiprocessing.Process(target=savedata, args=(p1,))
    t1.start()
    t2.start()
    
if __name__ == "__main__":
    main()
    