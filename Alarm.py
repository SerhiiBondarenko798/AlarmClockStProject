import kivy
import sys
from Time import Time 

class Alarm(Time):
	"""docstring for Alarm"""
	

	def SetAlarm(self, minutes, seconds):

		f=open("alarms.txt", "a+")
		try: 
			f.write("number: "+str(minutes)+":"+str(seconds)+"\n")
		except:
			print("Record unsuccesful")
		else:
			print("I recorded")
		finally:
			f.close()
			print("I closed a file")

