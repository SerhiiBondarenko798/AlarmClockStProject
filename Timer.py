import time
from Time import Time 

class Timer(Time):
	

	def setTimer(self,x):
		self.timertime = x+self.getTime()


	def CheckTimeTM (self,y):
		while True:
			count=self.timertime - time.time()
			print("%.10f" % count)
			time.sleep(1)
			if  count <= 0:
				#if self.timertime == 0:
				break
		return self.doAlarmTM()


	def doAlarmTM(self):
		print ("Ale, camon, ya tut zvenu")
		return False 
	


	def TimerTM(self):
		self.CheckTimeTM(self.timertime)

			

dd = Timer()
dd.setTimer(5)
dd.TimerTM()