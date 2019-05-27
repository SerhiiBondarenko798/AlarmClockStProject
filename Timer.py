import time

from Time import Time
	
class Timer(Time):

	def setTimer(self,minutes,seconds):
		print(minutes)
		print(seconds)
		x= minutes*60 + seconds
		
		self.timertime = x+self.getTime()
		# print(self.timertime)

	def CheckTimeTM (self):

		self.count=self.timertime - time.time()	
		if self.count<=0:
			print(0)
			return self.giveTime
		print("%.5f" % self.count)
		time.sleep(1)


		return self.CheckTimeTM()


	

	def doAlarmTM(self):
		print ("Ale, camon, ya tut zvenu")
		return False 
	


	def TimerTM(self):
		self.CheckTimeTM()
	def StopTM(self,value):
		self.status = value
	
	def giveTime(self, gived_value):
		pass

# d=Timer()
# d.setTimer(0,15)
# d.CheckTimeTM()