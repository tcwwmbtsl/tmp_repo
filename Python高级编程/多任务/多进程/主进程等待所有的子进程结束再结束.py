#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import time 


def task():
    for i in range(10):
        print("任务执行中。。。")
        time.sleep(0.2)

# 判断是否直接执行的模块
if __name__ == "__main__":
    # 创建子进程
    sub_process = multiprocessing.Process(target=task)
    sub_process.start()
    # 主进程退出，子进程销毁
    # 把子进程设置为守护主进程
    sub_process.daemon = True
    # 主进程延时 0.5 秒
    time.sleep(0.5)
    print('over')