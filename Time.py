import time
from abc import ABCMeta, abstractmethod, abstractproperty

class Itime:
	# def __init__(self,systime,sysdate,count,status):
	# 	self.systime = systime
	# 	self.sysdate = sysdate
	# 	self.count= count
	# 	self.status= status
	def getTime(self):
		pass

	def getDate(self):
		pass



class Time(Itime):
	
	def __init__(self):
		self.systime = time.time()
		self.sysdate = time.ctime(time.time())[4:10]
		self.count=0
		self.status = False

	def getTime(self):
		self.systime = time.time()
		return self.systime

	def getDate(self):
		self.sysdate = time.ctime(time.time())[4:10]
		return self.sysdate
        

		
       

		
