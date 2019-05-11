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

class Clocker(Label):
	"""docstring for Clocker"""
	def __init__(self, **kwargs):
		super(Clocker, self).__init__(**kwargs)
		with self.canvas.before:
			Color(0,1,0,1)
			Line(circle= (200, 350, 60), width = 1.5)


class BigRoundDickovina(FloatLayout):
	def __init__(self, **kwargs):
		super(BigRoundDickovina, self).__init__(**kwargs)
		pis = Clocker(text='00:00', pos_hint={'center_x':.5, 'center_y':.5})
		self.add_widget(pis)
		
      

		


class SC_Lables(AnchorLayout):
    def __init__(self, **kwargs):
        super(SC_Lables, self).__init__(**kwargs)
        self.img1=img1=Image(size_hint=(.5,.5), color = (0,1,1,1),mipmap=1)#<-----------------Место для функции смены пассивного цвета кнопки
        self.btn1 = btn1 =Button(background_color=(0,0,0,0))
        self.add_widget(img1,index=-1)
        self.add_widget(self.btn1)
        btn1.bind(on_press=self.ButtonON, on_release=self.ButtonOFF)
        with self.canvas.before:
            Color(.1, .1, .1, 1)#<-----------------Место для функции смены цвета бэка тулбара в пасивном состоянии
            self.rect = Ellipse(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def ButtonON(self,touch):
        self.img1.color =(0,0,0,1)#<-----------------Место для функции смены активного цвета кнопки
        with self.canvas.before:
            Color(0, 1, 1, 1)#<-----------------Место для функции смены цвета бэка тулбара в активном состоянии
            self.rect = Ellipse(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

    def ButtonOFF(self,touch):
        self.img1.color =(0,1,1,1)#<-----------------Место для функции смены пассивного цвета кнопки
        with self.canvas.before:
            Color(.1, .1, .1, 1)#<-----------------Место для функции смены цвета бэка тулбара в пасивном состоянии
            self.rect = Ellipse(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)


class StopClockWidget(FloatLayout):
	def __init__(self, **kwargs):
		super(StopClockWidget, self).__init__(**kwargs)

		self.play = play = SC_Lables(size_hint=(.15,.1), pos_hint={'x':0, 'y':0})
		# play.btn1.bind(on_release = pass)
		play.img1.source = "icons8-circled-play-filled-90.png"
		self.pause = pause = SC_Lables(size_hint=(.15,.1), pos_hint={'x':.2, 'y':0})

		pause.img1.source = "icons8-pause-button-filled-96.png"
		self.circle = circle = BigRoundDickovina(pos_hint={'center_x':.5, 'center_y':.5})
		self.add_widget(play)
		self.add_widget(pause)
		self.add_widget(circle)

	


class MainApp(App):
	def build(self):
		return StopClockWidget()


if __name__ == '__main__':
    MainApp().run()