#encoding=utf8

from threading import Event,Lock

class WorkQueue:
	
	def __init__(self,size):
		self.size = size
		self.values = []
		self.count = 0
		self.event = Event()
	
	#提交任务
	def addWork(self,work):
		if not work:
			return False
		lock = Lock()
		lock.acquire()
		if self.count == self.size :
			return False
		oldValues = self.values
		oldCount = self.count
		try:
			self.values.insert(0,work)
			self.count = oldCount + 1
			self.event.set()
			return True
		except Exception as exp :
			self.values = oldValues
			self.count = oldCount
		finally:
			lock.release()
	
	#获取任务
	def offer(self):
		lock = Lock()
		lock.acquire()
		oldCount = self.count
		try:
			if self.count > 0:
				self.count = oldCount -1
				return self.values.pop(0)
			else:
				self.event.wait(10)
				if self.count > 0:
					self.count = oldCount -1
					return self.values.pop(0)
				else:
					return None
		except Exception as exp:
			self.count = oldCount
		finally:
			lock.release()