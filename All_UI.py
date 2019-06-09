from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.bubble import Bubble
from kivy.uix.carousel import Carousel
from StopClock_UI import StopClockWidget
from Timer_UI import Timer_widget
from AlarmManager import AM_SM
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 700)
Config.set('graphics', 'resizable', 0)
# class Alarm_widget(Widget):
# 	"""docstring for Alarm_widget"""
# 	def __init__(self, arg):
# 		super(Alarm_widget, self).__init__()
# 		self.arg = arg
# Builder.load_file('AlarmClock.kv')




class AppBody(BoxLayout):
	def __init__(self, **kwargs):
		super(AppBody, self).__init__(**kwargs)
		with self.canvas.before:
			self.rect = Rectangle(size=self.size, pos=self.pos, source='chertov.jpg') #<-----------------Место для функции смены бэка
			self.bind(size=self._update_rect, pos=self._update_rect)
	def _update_rect(self, instance, value):
		self.rect.pos = instance.pos
		self.rect.size = instance.size

		




class HeaderLables(AnchorLayout):

    def __init__(self, **kwargs):
        super(HeaderLables, self).__init__(**kwargs)
        self.img1=img1=Image(size_hint=(.5,.5), color = (0,1,1,1),mipmap=1)#<-----------------Место для функции смены пассивного цвета кнопки
        self.btn1 = btn1 =Button(background_color=(0,0,0,0))
        self.add_widget(img1,index=-1)
        self.add_widget(self.btn1)
        btn1.bind(on_press=self.ButtonON, on_release=self.ButtonOFF)
        with self.canvas.before:
            Color(.1, .1, .1, 1)#<-----------------Место для функции смены цвета бэка тулбара в пасивном состоянии
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def ButtonON(self,touch):
    	self.img1.color =(0,0,0,1)#<-----------------Место для функции смены активного цвета кнопки
    	with self.canvas.before:
    		Color(0, 1, 1, 1)#<-----------------Место для функции смены цвета бэка тулбара в активном состоянии
    		self.rect = Rectangle(size=self.size, pos=self.pos)
    		self.bind(size=self._update_rect, pos=self._update_rect)

    def ButtonOFF(self,touch):
    	self.img1.color =(0,1,1,1)#<-----------------Место для функции смены пассивного цвета кнопки
    	with self.canvas.before:
    		Color(.1, .1, .1, 1)#<-----------------Место для функции смены цвета бэка тулбара в пасивном состоянии
    		self.rect = Rectangle(size=self.size, pos=self.pos)
    		self.bind(size=self._update_rect, pos=self._update_rect)
    	
      

		

class AlarmClockApp(App):
	
    def build(self):



    	MainAppWindow = AppBody(orientation='vertical')
    	ToolBar=Bubble(size_hint=[1, .1])
    	MainAppWindow.add_widget(ToolBar)
    	WorkArea = AnchorLayout()
    	MainAppWindow.add_widget(WorkArea)



    	self.Timer_icon= Timer_icon = HeaderLables(size_hint=[1/5, 1])
    	Timer_icon.img1.source='icons8-alarm-clock-96.png'
    	Timer_icon.btn1.bind(on_release=self.GoTOTimer_widget)

    	self.Stopclock_widget= Stopclock_widget = HeaderLables(size_hint=[1/5, 1])
    	Stopclock_widget.img1.source='icons8-sport-stopwatch-96.png'
    	Stopclock_widget.btn1.bind(on_release=self.GoTOStopclock_widget)

    	self.Alarm_widget= Alarm_widget = HeaderLables(size_hint=[1/5, 1])
    	Alarm_widget.img1.source='icons8-alarm-96.png'
    	Alarm_widget.btn1.bind(on_release=self.GoTOAlarm_widget)

    	self.Cust_widget= Cust_widget = HeaderLables(size_hint=[1/5, 1])
    	Cust_widget.img1.source='icons8-star-96.png'
    	Cust_widget.btn1.bind(on_release=self.GoTOCust_widget)

    	self.Settings_widget= Settings_widget = HeaderLables(size_hint=[1/5, 1])
    	Settings_widget.img1.source='icons8-settings-96.png'
    	Settings_widget.btn1.bind(on_release=self.GoTOSettings_widget)
    		

    	ToolBar.add_widget(Timer_icon)
    	ToolBar.add_widget(Stopclock_widget)
    	ToolBar.add_widget(Alarm_widget)
    	ToolBar.add_widget(Cust_widget)
    	ToolBar.add_widget(Settings_widget)
    	
    	self.myTimer=Timer_widget()
    	self.myStopClock=StopClockWidget()
    	self.myAM=AM_SM()
    	carousel=Carousel(direction='right')
    	carousel.add_widget(self.myTimer)
    	carousel.add_widget(self.myStopClock)
    	carousel.add_widget(self.myAM)
    	WorkArea.add_widget(carousel)
    	return MainAppWindow
    def GoTOTimer_widget(self,touch):#<-----------------Место для функции перехода на таймер виджет
    	return print('Time to timer')
    def GoTOStopclock_widget(self,touch):#<-----------------Место для функции перехода на стопклок виджет
    	return print('Time to stopclock')
    def GoTOAlarm_widget(self,touch):#<-----------------Место для функции перехода на аларм виджет
    	return print('Time to alarmclock')
    def GoTOCust_widget(self,touch):#<-----------------Место для функции перехода на каст виджет
    	return print('Time to customise')
    def GoTOSettings_widget(self,touch):#<-----------------Место для функции перехода на сетингс виджет
    	return print('Time to setings')
   

if __name__ == '__main__':
    AlarmClockApp().run()




# class app_lable(Widget):
# 	def __init__(self, **arg):
# 		super(app_lable, self).__init__(**arg)
# 		self.arg = arg
# 		self.vs_image = Image(source='gfbr.png', color = (1,0,1,1))
# 		self.invs_button = Button(text='Hello world', font_size=5, background_color =(1,1,0,1))
# 		  #     with self.canvas.before:
#     #         Color(0, 1, 0, 1)  # green; colors range from 0-1 instead of 0-255
#     #         self.rect = Rectangle(size=self.size, pos=self.pos)

#     #     self.bind(size=self._update_rect, pos=self._update_rect)

#     # def _update_rect(self, instance, value):
#     #     self.rect.pos = instance.pos
#     #     self.rect.size = instance.size
# 	def setimage(self,path):
# 		self.vs_image.source = path


		
# #self.body = FloatLayout()
# self.body.add_widget(self.vs_image)
# self.body.add_widget(self.invs_button)
# # Image(source='gfbr.png', color = (0,0,1,1),)
