import time
from Time import Time 



class NewPrint(Exception):
	"""docstring for NewPrint"""
	def __init__(self,value):
		self.value = value


class StopClock(Time):


	def startSC(self, *args, **kwargs):
			self.count = time.time()-self.getClockTime() 
		

			# if self.pauseSC():
			# 	print(count)
			# 	while True:
			# 		#time.sleep(1)
			# 		if self.continueSC():    #тут тоже функция вместо кнопки
			# 			break

			# if self.endSC(count): #тут будет условие нажатия кнопки, а сейчас может выдавать ошибку ибо функция endSC не написана
			# 	break
			

	def pauseSC(self):
		return True

	def endSC(self,count):
		count = 0
		return True

	def continueSC(self):
		return True


