import time

from Time import Time
	
class Timer(Time):

	def setTimer(self,minutes,seconds):
		print(minutes)
		print(seconds)
		self.x= minutes*60 + seconds
		
		self.timertime = self.x+self.getTime()
		# print(self.timertime)

	def CheckTimeTM (self, *args, **kwargs):

		self.count=self.timertime - time.time()	
		
		print(str(int(self.count//60))+":"+str(int(self.count%60)))


		return self.giveTime#teresh pidor otday svoy kletchatie shtani, oni top


	

	def doAlarmTM(self):
		print ("Ale, camon, ya tut zvenu")
		return False 
	


	def TimerTM(self, min, sec):
		self.setTimer(min,sec)
		self.CheckTimeTM()
	def StopTM(self,value):
		self.status = value
	
	def giveTime(self, *args, **kwargs):
		pass

# d=Timer()
# d.setTimer(0,15)
# d.CheckTimeTM()