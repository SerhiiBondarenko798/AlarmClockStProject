import time
from Time import Time
	
class Timer(Time):
	

	def setTimer(self,minutes,seconds):
		print(minutes)
		print(seconds)
		x= minutes*60 + seconds
		
		self.timertime = x+self.getTime()
		# print(self.timertime)

	def CheckTimeTM (self, count):
		self.count=self.timertime - time.time()			
		print("%.10f" % self.count)
		time.sleep(1)

		if self.count<=0:
			return False
		return self.CheckTimeTM(self.count)

		


	def doAlarmTM(self):
		print ("Ale, camon, ya tut zvenu")
		return False 
	


	def TimerTM(self):
		self.CheckTimeTM()
	def StopTM(self,fuckoff):
		self.status = fuckoff


	def giveTime(self, gived_value):
		pass