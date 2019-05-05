import time
from Time import Time 	
class Timer(Time):
	

	def setTimer(self,minutes,seconds):
		print(minutes)
		print(seconds)
		x= minutes*60 + seconds
		print (x)
		
		self.timertime = x+self.getTime()


	def CheckTimeTM (self,y):
		while True:
			count=self.timertime - time.time()
			# print("%.10f" % count)
			# time.sleep(1)
			if  (count <= 0):
				
				break
			elif (self.status):
				break

		return self.doAlarmTM()


	def doAlarmTM(self):
		print ("Ale, camon, ya tut zvenu")
		return False 
	


	def TimerTM(self):
		self.CheckTimeTM(self.timertime)
	def StopTM(self,fuckoff):
		self.status = fuckoff


