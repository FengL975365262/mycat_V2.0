#encoding=utf-8

from threading import Thread
import time

class ThreadPool:

        def __init__(self, init_thread_num , work_queue):
			self.isRunning = False
			self.run = run
            self.threads = []
            self.init_thread_num = init_thread_num
            self.max_thread_num = 8
            self.work_queue = work_queue
            self.alive_thread_num = init_thread_num
            self.wait_thread_num = init_thread_num
            self.max_wait_time = 300 #second

        def start_thread_pool(self,work):
            for i in range(self.init_thread_num):
                self.threads[i] = Thread()
                self.threads[i].run = work
            self.execute()
			
		'''调用线程分配任务'''
        def execute(self):
            while self.work_queue.offer() :
				
		
		'''执行任务'''
		def dowork(self,thread,work):
			while self.isRunning:
				
			
		def addthread(self):
		
		def delthread(self):
		
		
