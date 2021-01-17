#!/usr/bin/python
#coding:utf-8
import threading
import Queue
import time
#q是任务队列
#NUM是并发线程总数
#JOBS是有多少任务
q = Queue.Queue()
NUM = 3
JOBS = 10
A = {}
#具体的处理函数，负责处理单个任务
def do_somthing_using(arguments):
    print arguments
    time.sleep(3)
    A[arguments] = time.strftime('%H:%M:%S')
#这个是工作进程，负责不断从队列取数据并处理
def working():
    while True:
        arguments = q.get()
        do_somthing_using(arguments)
        q.task_done()
#fork NUM个线程等待队列
for i in range(NUM):
    t = threading.Thread(target=working)
    t.setDaemon(True)
    t.start()
#把JOBS排入队列
for i in range(JOBS):
    q.put(i)
#等待所有JOBS完成
q.join()

print A
