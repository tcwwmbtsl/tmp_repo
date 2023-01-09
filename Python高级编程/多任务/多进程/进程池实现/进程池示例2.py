#!/usr/bin/env python
# coding=utf-8
from multiprocessing import Pool
import os
import time
import random


def worker(a):
    t_start = time.time()
    print('%s开始执行,进程号为%d' % (a, os.getpid()))

    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(a, "执行完成,耗时 %0.2f" % (t_stop - t_start))


if __name__ == "__main__":
    po = Pool(3)
    for i in range(10):
        po.apply_async(worker, (i, ))
    print("--start--")
    po.close()
    po.join()
    print("--end--")
