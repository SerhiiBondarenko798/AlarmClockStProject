import time
from Time import Time 



class NewPrint(Exception):
	"""docstring for NewPrint"""
	def __init__(self,value):
		self.value = value


class StopClock(Time):


	def startSC(self, count):

		while True:
			count = time.time()-self.getClockTime() 
			time.sleep(1)
			print("%.1f" % count)
			try:
				if count>=float(4):
					print('sasat')
					raise NewPrint(0)
			except NewPrint as npr:
				self.startSC(npr.value)
				print('dodo')
			

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



dd = StopClock()
dd.startSC(0)
time.sleep(1)