# encoding=utf-8

from threading import Thread
import time
from tools import queue


class ThreadPool:

    def __init__(self):
        self.threads = []
        self.init_thread_num = 1
        self.max_thread_num = 8
        self.work_queue = queue.WorkQueue(80)
        self.error_queue = queue.WorkQueue(40)
        self.alive_thread_num = 0
        self.max_wait_time = 300

    def initThreadPool(self):
        for i in range(self.init_thread_num):
            thread = Thread(None, self.work, args=(i,))
            thread.isRunning = True
            self.threads.append(thread)
            thread.start()
            self.alive_thread_num += 1

    def addWorker(self, num):
        addNum = num if num <= self.max_thread_num - self.alive_thread_num else self.max_thread_num - self.alive_thread_num
        for i in range(addNum):
            thread = Thread(None, self.work, args=(i + self.alive_thread_num,))
            thread.isRunning = True
            self.threads.append(thread)
            thread.start()
            self.alive_thread_num += 1

    def removeWorker(self, num):
        rmNum = num if num <= self.alive_thread_num - self.init_thread_num else self.alive_thread_num - self.init_thread_num
        for i in range(rmNum):
            index = len(self.threads) - i
            self.threads[index].isRunning = False

    def execute(self, job):
        if len(self.threads) == 0 : self.initThreadPool()
        if job:
            self.work_queue.addWork(job)
            self.checkThreads()

    def checkThreads(self):
        changeNum = int(self.work_queue.count / (self.work_queue.size/self.max_thread_num)) - self.alive_thread_num
        if changeNum > 0:
            self.addWorker(changeNum)
        elif changeNum < 0:
            self.removeWorker(-changeNum)

    def work(self, index):
        while self.threads[index].isRunning:
            job = self.work_queue.offer()
            if job:
                try:
                    job.run()
                except Exception as exp:
                    self.error_queue.addWork(job)
                    raise exp
            self.checkThreads()
        self.threads.remove(self.threads[index])
        self.alive_thread_num -= 1