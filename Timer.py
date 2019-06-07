import time
from Time import Time
	
class Timer(Time):

	def setTimer(self,minutes,seconds):
		# print(minutes)
		# print(seconds)
		self.x= minutes*60 + seconds
		
		self.timertime = self.x+self.getTime()
		# self.count=self.timertime - time.time()
		# print(self.timertime)

	def CheckTimeTM (self, *args, **kwargs):
		# if self.count != 0:
			# print('sosi')
			# self.timertime = self.count
		self.count=self.timertime - time.time()	
		self.count=round(self.count)
		# print(str(self.count//60)+":"+str(self.count%60))


		# return self.giveTime#teresh pidor otday svoy kletchatie shtani, oni top


	

	def doAlarmTM(self):
		print ("Ale, camon, ya tut zvenu")
		
	


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