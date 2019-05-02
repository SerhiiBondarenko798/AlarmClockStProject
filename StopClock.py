import time
from Time import Time 

class StopClock(Time):


	def startSC(self):
		while True:
			count = time.time()-self.getTime()
			print("%.1f" % count)
			time.sleep(1)
			if self.pauseSC():
				print(count)
				while True:
					#time.sleep(1)
					if self.continueSC():    #тут тоже функция вместо кнопки
						break

			if self.endSC(count): #тут будет условие нажатия кнопки, а сейчас может выдавать ошибку ибо функция endSC не написана
				break
			

	def pauseSC(self):
		return True

	def endSC(self,count):
		count = 0
		return True

	def continueSC(self):
		return True



dd = StopClock()
dd.startSC()
time.sleep(1)