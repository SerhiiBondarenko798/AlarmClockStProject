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
		if self.count<=0:
			print(0)
			return self.giveTime
		print("%.5f" % self.count)
		time.sleep(0.1)


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