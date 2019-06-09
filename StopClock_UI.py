from StopClock import StopClock

import kivy
import asyncio
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.button import Button
from kivy.clock import Clock
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
from kivy.factory import Factory
from kivy.animation import Animation
from kivy.clock import Clock, mainthread
from kivy.uix.gridlayout import GridLayout
import threading
import sys 
import trace
import time
import types
from Time import Time 

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 700)
Config.set('graphics', 'resizable', 0)


shouldRun = False

class Clocker(Label):
    """docstring for Clocker"""
    def __init__(self, **kwargs):
        super(Clocker, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0,1,1,1)
            Line(circle= (200, 350, 100), width = 1.5)


class BigRoundDickovina(FloatLayout):
    def __init__(self, **kwargs):
        super(BigRoundDickovina, self).__init__(**kwargs)
        self.pis = Clocker(text=' ', pos_hint={'center_x':.5, 'center_y':.5}, font_size = 50, color=(0,1,1,1))
        self.add_widget(self.pis)
        
      
class Act_Time_Screen(FloatLayout):
    def __init__(self, **kwargs):
        super(Act_Time_Screen, self).__init__(**kwargs)
        self.SCWindow=SCWindow=BigRoundDickovina()
        self.add_widget(SCWindow)
        


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
        
        SC_Body=FloatLayout(pos_hint={'center_x':0.5,'y':0})
        self.SCSession= SCSession = StopClock() 

        self.Button_Start= Button_Start= SC_Lables(size_hint=[1/5.5,1],pos_hint={'x': 0.1, 'y': 0})
        Button_Start.img1.source='icons8-circled-play-filled-90.png'
        Button_Start.btn1.bind(on_release=self.LetsGetStart)

        Button_Pause= SC_Lables(size_hint=[1/5.5,1],pos_hint={'center_x': .5, 'y': 0})
        Button_Pause.img1.source='icons8-pause-button-filled-96.png'
        Button_Pause.btn1.bind(on_release=self.LetsGetPause)

        Button_Stop= SC_Lables(size_hint=[1/5.5,1],pos_hint={'right': 0.9, 'y': 0})
        Button_Stop.img1.source='icons8-no-96.png'

        Button_Stop.btn1.bind(on_release=self.LetsGetStop)
        


       
      

        self.circle = circle = Act_Time_Screen()
        

        SC_ToolBar=FloatLayout(size_hint=(.9,.1),pos_hint={'center_x':0.5,'y':0})
        SC_ToolBar.add_widget(Button_Start)
        SC_ToolBar.add_widget(Button_Pause)
        SC_ToolBar.add_widget(Button_Stop)



        SC_Body.add_widget(circle)
        SC_Body.add_widget(SC_ToolBar)

        self.add_widget(SC_Body)
    def LetsGetStart(self, touch):
        global shouldRun
        shouldRun = True
        self.my_thread=threading.Thread(target=self.second_thread, args=(self.circle.SCWindow.pis.text,self.SCSession.count))
        self.my_thread.start()


    def LetsGetPause(self,touch):
        global shouldRun
        shouldRun = False
        print("my time"+str(self.SCSession.count))
        
        self.Button_Start.btn1.bind(on_release=self.LetsGetContinue)
    def LetsGetContinue(self, touch):
        global shouldRun
        self.SCSession.pauseSC()

        shouldRun = True
        
    def LetsGetStop(self, touch):
        global shouldRun
        shouldRun = False
        self.SCSession.pauseSC()
        self.SCSession.endSC(self.SCSession.count)
        self.update_label_text("0:0.0")
        print ("ended")



    @mainthread
    def update_label_text(self,new_text):
        self.circle.SCWindow.pis.text=new_text
       

    def second_thread(self,l_text, seconds,*args,**kwargs):
            global shouldRun
    
            while self.SCSession.count>=0:
                if shouldRun == False:
                    
                    print("vse")
                    break
                self.SCSession.startSC(seconds)
                self.update_label_text(str(int(self.SCSession.count//60))+":"+str(round(self.SCSession.count%60, 1)))
                print(str(int(self.SCSession.count)))
                time.sleep(0.1)  

class ICommand:
    def __init__(self, func = None):
        self.__func = func

    def execute(self, *args, **kwargs):
        pass

class CommandInputed(ICommand):
    def __init__(self, func = None):
        super(CommandInputed, self).__init__(func)
        self.__func=func

    def execute(self,this, *args, **kwargs):
        # inputingprocess(self.valueminutes,self.valueseconds)
        if self.__func:
            return self.__func(*args, **kwargs)
        return None

# class MainApp(App):
#     def build(self):
#         return StopClockWidget()


# if __name__ == '__main__':
#     MainApp().run()