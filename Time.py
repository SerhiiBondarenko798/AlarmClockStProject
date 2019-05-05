import time

class Time:
	
	def __init__(self):
		self.systime = time.time()
		self.sysdate = time.ctime(time.time())[4:10]
		self.status = False

	def getTime(self):
		return self.systime

	def getDate(self):
		return self.sysdate
        

		
       

		
