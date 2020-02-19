# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:06:13 2020

@author: hp
"""

from multiprocessing import Process, Manager
import multiprocessing as mtp
import time
cores = mtp.cpu_count()
print(cores)


def process_each_part(lists, part_n):
    lists.append(list(map(lambda x:x**2, part_n)))


if __name__ == '__main__':
    manager = Manager()
    lists = manager.list()
    li = [i for i in range(10000000000, 0, -1)]
    per_core = len(li)//cores
    processes = []
    start = time.time()
    for index in range(cores):
        print(index)
        part_n = li[per_core*index : per_core*(index+1)]
        p = Process(target = process_each_part, args = (lists, part_n))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    end = time.time()
    #print(lists)
    print(end-start)