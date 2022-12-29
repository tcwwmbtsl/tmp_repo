#!/usr/bin/env python
# coding=utf-8


import multiprocessing 
import time 


# 定义合局变量
g_list = list()


# 添加数据的任务
def add_data():
    for i in range(3):
        # 列表是可变类型，可以在原有内存的基础上修改数据，并且修改后内存地址不变，所以不需要用 global 来声明
        g_list.append(i)
        print(f"add {i}")
        time.sleep(0.2)
        
def read_data():
    print("read:",  g_list)
# 解决 windows 递归创建进程
# 1、防止别人导入文件的时候执行 main 里面的代码
# 2、防止windows 系统递归创建子进程
if __name__ == "__main__":
    # 添加数据的子进程
    add_process = multiprocessing.Process(target=add_data)

    # 读取数据的子进程
    read_process = multiprocessing.Process(target=read_data)

    # 启动进程任务
    add_process.start()
    add_process.join()
    read_process.start()