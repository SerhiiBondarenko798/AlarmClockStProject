import time

class Time:
	
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
        

		
       

		
