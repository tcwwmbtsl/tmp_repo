#!/usr/bin/env python
# coding=utf-8

from audioop import mul
import multiprocessing


def process(index):
    print(f'Process:{index}')


if __name__ == "__main__":
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i, ))
        p.start()
