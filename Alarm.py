import kivy
import sys
from Time import Time 

class Alarm(Time):
	"""docstring for Alarm"""
	

	def SetAlarm(self, minutes, seconds):

		f=open("alarms.txt", "a+")
		
		# try:
		# 	index=int(f.read(0))+1
		# except ValueError:
		# 	index = 1
		index = self.ReadAlarm()+1

		try:
			if (minutes<=9) & (seconds<=9):
				f.write("alarm №"+str(index)+":0"+str(int(minutes))+":0"+str(int(seconds))+"\n")
			elif minutes<=9:
				f.write("alarm №"+str(index)+":0"+str(int(minutes))+":"+str(int(seconds))+"\n")
			elif seconds<=9:
				f.write("alarm №"+str(index)+":"+str(int(minutes))+":0"+str(int(seconds))+"\n")
			else:
				f.write("alarm №"+str(index)+":"+str(int(minutes))+":"+str(int(seconds))+"\n")
		except:
			print("Record unsuccesful")
		else:
			print("I recorded")
		finally:
			f.close()
			print("I closed a file")

	def ReadAlarm(self):
		f=open("alarms.txt", "a+")
		i=0
		for line in f: 
			line 
			i=i+1

		
		print(i)
		f.close()
		return i


Alarm().ReadAlarm()
