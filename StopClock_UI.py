import kivy
import time
from kivy.app import App

from StopClock import StopClock
from Time import Time 

from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image


from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from kivy.config import Config
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 700)
Config.set('graphics', 'resizable', 0)

class EllipseClock(Widget):
	def __init__(self, **kwargs):
		super(EllipseClock, self).__init__(**kwargs)
		
	# def updateTime(self, *args):
		
		# self.dady = str(time.clock())
		with self.canvas.before:
			Color(1,0,0,1)
			
			Ellipse(circle=(200, 300, 70),pos=(150,350),color=(0,0,0,1), width = 1.5, index = -1)
			
		
# 		# self.dady = str(time.clock())
# 		
		# with self.canvas:
		# 	Line(circle=(200, 300, 70), color = (0,1,0,1), width = 1.5, pos=(100,400))

	 
	# def start_tw(self, touch):
	# 	return StopClock().startSC()





class Tab(Label):
	def updateTime(self, *args):
		self.dady = str(StopClock().startSC())
		with self.canvas:
			Color(0,1,0,1)
			Label(text = self.dady, pos=(100, 330))
	

class StopClock_UI(App, StopClock):
	def build(self):

		pisos = StopClock()
		

		
		me = Widget()
		me.add_widget(EllipseClock())
		
		
		
		
        


		startSC_widget = Widget()
		startSC_button = Button(pos = (30,350), border = (2,2,2,2))
		startSC_button.bind(on_release = self.start)
		startSC_widget.add_widget(startSC_button)
		startSC_widget.add_widget(Image(source='Icons/stopclock_timer/icons8-circled-play-filled-90.png', size_hint=(.5,.5), pos=startSC_button.pos, color = (0, 1, 0, 1), mipmap=1), index =-1)
		
		pauseSC_widget = Widget()
		
		pauseSC_image = Image(source='Icons/stopclock_timer/icons8-pause-button-filled-96.png', size_hint=(.5,.5), pos= (270, 350) ,color = (0, 1, 0, 1), mipmap=1)
		pauseSC_button = Button(pos = pauseSC_image.pos, size_hint = pauseSC_image.size)
		pauseSC_button.bind(on_press = self.pause)
		pauseSC_widget.add_widget(pauseSC_button)
		pauseSC_widget.add_widget(pauseSC_image, index =-1)
		
		# 
		# Clock.schedule_interval(t.updateTime, 1)
		
		# me.add_widget(t(pos=(100,100)))



		me.add_widget(startSC_widget)
		me.add_widget(pauseSC_widget)

		return me

	

	def start(self, touch):
		t = Tab()
		Clock.schedule_interval(t.updateTime, 0.1)
		return t
		
		# Clock.schedule_interval(StopClock().startSC(), 1)

	
		
		 
		

	def pause(self, touch):
		return StopClock().pauseSC()


StopClock_UI().run()
	