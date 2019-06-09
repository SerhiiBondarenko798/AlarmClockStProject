import kivy
import asyncio
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.bubble import Bubble
from kivy.uix.screenmanager import ScreenManager, Screen,WipeTransition,SlideTransition
from kivy.uix.image import Image
from kivy.graphics import (Color, Ellipse, Rectangle, Line,BorderImage)
from kivy.uix.recycleview import RecycleView
from kivy.uix.splitter import Splitter
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from abc import ABCMeta, abstractmethod, abstractproperty, ABC
from abstract_classes import I_input_getTime, I_Button
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.factory import Factory
from kivy.animation import Animation
from kivy.clock import Clock, mainthread
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
import threading
import sys 
import trace
import time
import types
from Time import Time 
from Timer import Timer

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 700)
Config.set('graphics', 'resizable', 0)


class Alarm_manager_Lables(AnchorLayout):
    def __init__(self, **kwargs):
        super(Alarm_manager_Lables, self).__init__(**kwargs)
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
# class Alarm_manager_bar(ScrollView):
# 	def add_widget_to(self,inst):
# 		self.add_widget(inst)
class AM_SM(ScreenManager):

    def __init__(self, **kwargs):
        super(AM_SM, self).__init__(**kwargs)
        # self.snovadarou=snovadarou=Set_Time_Screen()
        # self.add_widget(snovadarou)		

class Alarm_manager_widget(FloatLayout):
	def __init__(self, **kwargs):
		super(Alarm_manager_widget, self).__init__(**kwargs)
		# self.Alarm_Body=Alarm_Body=FloatLayout(pos_hint={'center_x':0.5,'y':0})
		self.AM_bar=AM_bar=ScrollView(size_hint=(1,.9),pos_hint={'center_x':0.5,'top':1})
		self.add_widget(AM_bar)
		self.AM_ToolBar=FloatLayout(size_hint=(.9,.1),pos_hint={'center_x':0.5,'y':0})
		self.Button_Add=Alarm_manager_Lables(size_hint=[1/4,1],pos_hint={'center_x': .5, 'y': 0})
		self.Button_Add.img1.source='icons8-circled-play-filled-90.png'
		self.AM_ToolBar.add_widget(self.Button_Add)
		self.add_widget(self.AM_ToolBar)
		# self.add_widget(Alarm_Body)
	def LetsGetSAdd(self, touch,inst):
		pass
	
   
   # self.AlarmSession.StopTM(True)
class MainApp(App):
	def build(self):
		return Alarm_manager_widget()

class Alarm_widget(FloatLayout):
    def __init__(self, **kwargs):
        super(Alarm_widget, self).__init__(**kwargs)
        # Alarm_Body=FloatLayout(pos_hint={'center_x':0.5,'y':0})
        self.DataBar = DataBar  =BoxLayout(size_hint=[.7,1],pos_hint={'x':0,'center_y':0.5}, orientation='vertical')
        self.frst=frst=Label(text='Alarm1')
        self.scnd=scnd=DataTime(text='0:0')

        DataBar.add_widget(frst)
        DataBar.add_widget(scnd)
        self.add_widget(DataBar)
        self.ONOFF= ONOFF= Switch(acitve=LetsGetActivate)
        self.Alarm_ToolBar=Alarm_ToolBar=FloatLayout(size_hint=(.4,1),pos_hint={'right':1,'center_y':0.5})
        self.Button_Delete=Button_Delete= AlarmLables(size_hint=[1/5.5,1],pos_hint={'right': 0.9, 'y': 0})
        Button_Delete.img1.source='icons8-no-96.png'
        Alarm_ToolBar.add_widget(Button_Delete)
        # Button_Stop.btn1.bind(on_release=self.LetsGetDelete)
        self.add_widget(Alarm_ToolBar)
    def LetsGetActivate(self,touch):
    	pass

        # self.AlarmSession= AlarmSession = Alarm()


if __name__ == '__main__':
    MainApp().run()