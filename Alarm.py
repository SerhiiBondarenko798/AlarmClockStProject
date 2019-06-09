
import sys
from Time import Time 

class Alarm(Time):
	"""docstring for Alarm"""
	

	def SetAlarm(self, minutes, seconds):

		f=open("alarms.txt", "r")
		
		# try:
		# 	index=int(f.read(0))+1
		# except ValueError:
		index = 0
		
		for line in f:
			try: 
				index = int(self.ReadAlarm(line))
				print("index"+str(index))
			except IndexError:
								
				break
		f.close()
		index = index+1
		print("index"+str(index))
		f=open("alarms.txt", "a+")


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

	def ReadAlarm(self,line):
		# try:
		# 	# f=open("alarms.txt", "r")
		# except:
		# 	print("no")
		# else:
			
			# line=f.readline()
			
			i=line[7]
			print(i)
			# f.close()
			return i
	def ReadMinutes(self,line):
		# try:
		# 	f=open("alarms.txt", "r")
		# except:
		# 	print("no")
		# else:
			# line=f.readline()
			mun=line[9:11]
			print (mun)
			# f.close()
			return mun
			
			
			
	def ReadSeconds(self,line):
		# try:
		# 	f=open("alarms.txt", "r")
		# except:
		# 	print("no")
		# else:
			# line=f.readline()
			sec=line[12:14]
			print (sec)
			# f.close()
			return sec
			
			
					


