import kivy
import asyncio
from Alarm_UI import SetAlarm_widget,AlarmLables
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
from Alarm import Alarm
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
class AM_SM(FloatLayout):

    def __init__(self, **kwargs):
        super(AM_SM, self).__init__(**kwargs)
        self.AlMa=AlMa=ScreenManager(size_hint=[1,1],pos_hint={'center_x':0.5,'top':1})
        self.scnd=scnd=SetAlarm_widget(name='SAW',id='firstw')
        # self.thd=thd=Call_Time_Screen(name='CTS',id='thdw')
        self.Button_Add=Alarm_manager_Lables(size_hint=[1/4,.1],pos_hint={'center_x': .5, 'y': 0})
        self.Button_Add.img1.source='icons8-circled-play-filled-90.png'
        self.Button_Add.btn1.bind(on_release=self.LetsGetAdd)
        
        self.Button_Start=Button_Start= AlarmLables(size_hint=[1.5/5.5,1.5],pos_hint={'x': 0.35, 'y': 0.1})
        Button_Start.img1.source='icons8-circled-play-filled-90.png'
        Button_Start.btn1.bind(on_release=self.scnd.LetsGetStart)

        self.frst=frst=Alarm_manager_widget(name='AMW',id='scndw')
        self.AlMa.add_widget(frst)
        if self.frst.kuku:
        	print('zvuk')
        	
        self.scnd.Alarm_ToolBar.add_widget(self.Button_Start)
        self.frst.add_widget(self.Button_Add)
        self.AlMa.add_widget(scnd)
        # self.AlMa.add_widget(thd)
        self.add_widget(AlMa)
    def LetsGetAdd(self, touch):
    	self.AlMa.transition.direction = 'left'
    	self.AlMa.current = 'SAW'
        # self.snovadarou=snovadarou=Set_Time_Screen()
        # self.add_widget(snovadarou)		


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


class Call_Time_Screen(FloatLayout):
    def __init__(self, **kwargs):
        super(Call_Time_Screen, self).__init__(**kwargs)
        self.CallMsgBar=CallMsgBar=CallMsgBody(size_hint=[.9,.8],pos_hint={'center_x':0.5,'top':1})
        self.add_widget(CallMsgBar)
        self.CWindow=CWindow=BoxLayout(size_hint=[.9,.2],pos_hint={'center_x':0.5,'y':0})
        self.CallAgreeButt=CallAgreeButt=CallButt(size_hint=[1/2,1],pos_hint={'x': 0, 'y': 0})
        self.CallDAgreeButt=CallDAgreeButt=CallButt(size_hint=[1/2,1],pos_hint={'right': 1, 'y': 0})
        CWindow.add_widget(CallAgreeButt)
        CWindow.add_widget(CallDAgreeButt)
        self.add_widget(CWindow)
        
class CallMsgBody(Label):
    def __init__(self,**kwargs):
        super(CallMsgBody, self).__init__(**kwargs)
        self.text ='Sudar,pryamo seychas washe utroistvo\n izdayot nepriyatniy zvuk,\n recomenduyu chto-to s etim sdelat!'
        self.font_size = 15
        with self.canvas.before:
            Color(0, 1, 1, 1) 
class CallButt(AnchorLayout):

    def __init__(self, **kwargs):
        super(CallButt, self).__init__(**kwargs)
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
        
        



class Alarm_manager_widget(Screen):
	def __init__(self, **kwargs):
		super(Alarm_manager_widget, self).__init__(**kwargs)
		# self.Alarm_Body=Alarm_Body=FloatLayout(pos_hint={'center_x':0.5,'y':0})
		self.AM_bar=AM_bar=BoxLayout(orientation='vertical')
		self.scroller=scroller=ScrollView(size_hint=(1,.9),pos_hint={'center_x':0.5,'top':1})
		scroller.add_widget(AM_bar)
		self.add_widget(scroller)
		self.f=f=open("alarms.txt", "r")
		self.Alarm_one =Alarm_one= Alarm()

		# AM_bar.add_widget(Alarm_widget(size_hint=(1,None),height=100))
		


		

		for line in f:
			print (line)
			try:
				self.Create_Alarm(Alarm_one.ReadMinutes(line), Alarm_one.ReadSeconds(line) , Alarm_one.ReadAlarm(line))
			except IndexError:
				break

		f.close()
		self.AM_ToolBar=FloatLayout(size_hint=(1,.1),pos_hint={'center_x':0.5,'y':0})
		self.add_widget(self.AM_ToolBar)
		self.kuku=BooleanProperty(False)
	
		 # self.add_widget(Alarm_Body)
	def Create_Alarm(self,mint,secd,inde):
		korobka=Alarm_widget()
		# x= int(mint)*60 + int(secd)
		korobka.frst.text='Alarm №'+inde
		korobka.scnd.text=mint+':'+secd
		self.scroller.remove_widget(self.AM_bar)
		self.scroller.add_widget(self.AM_bar)
		self.AM_bar.add_widget(korobka)
		
	
   
   # self.AlarmSession.StopTM(True)
# class MainApp(App):
# 	def build(self):
# 		return AM_SM()

class Alarm_widget(FloatLayout):
    def __init__(self, **kwargs):
        super(Alarm_widget, self).__init__(**kwargs)
        # Alarm_Body=FloatLayout(pos_hint={'center_x':0.5,'y':0})
        self.DataBar = DataBar  =BoxLayout(size_hint=[.5,1],pos_hint={'x':0,'center_y':0.5}, orientation='vertical')
        self.frst=frst=Label(text='Alarm1')
        self.scnd=scnd=Label(text='0:0')
        self.size_hint=(1,None)
        self.height=100
        self.sound_inst_loop=['Sound1.mp3','Sound2.mp3','Sound3.mp3','Sound4.mp3','Sound5.mp3']
        self.sound_loop=['1','2','3','4','5']
        for i in range(len(self.sound_inst_loop)):
            self.sound_loop[i] = SoundLoader.load(self.sound_inst_loop[i])
        self.touchedS=BooleanProperty(False)
        self.audiobool=BooleanProperty(False)
        DataBar.add_widget(frst)
        DataBar.add_widget(scnd)
        self.callScr=Call_Time_Screen()
        self.popupsi=Popup(title='Unexpected/uninputed value',content=self.callScr)
        self.add_widget(DataBar)
        self.ONOFF= ONOFF= Switch(size_hint=[1/2,.5],pos_hint={'x': 0, 'center_y': 0.5})
        ONOFF.bind(active=self.LetsGetActivate)
        self.Alarm_ToolBar=Alarm_ToolBar=FloatLayout(size_hint=(.5,1),pos_hint={'right':1,'center_y':0.5})
        # self.Button_Delete=Button_Delete= Alarm_manager_Lables(size_hint=[1/5,.4],pos_hint={'right': .9, 'center_y': 0.5})
        # Button_Delete.img1.source='icons8-no-96.png'
        # Button_Delete.btn1.bind(on_release=self.LetsDelete)
        Alarm_ToolBar.add_widget(ONOFF)
        # Alarm_ToolBar.add_widget(Button_Delete)
        # Button_Stop.btn1.bind(on_release=self.LetsGetDelete)
        self.add_widget(Alarm_ToolBar)
    def LetsGetActivate(self,*args, **kwargs):
    	if self.ONOFF.active:
    		self.TimerSession=Timer()
    		self.callScr.CallAgreeButt.img1.source='icons8-circled-play-filled-90.png'
    		self.callScr.CallAgreeButt.btn1.bind(on_release=self.IDAgree)
    		self.callScr.CallDAgreeButt.img1.source='icons8-no-96.png'
    		self.callScr.CallDAgreeButt.btn1.bind(on_release=self.IAgree)
    		strat = CommandInputed(self.inputingprocess)
    		strat.execute(self,int(self.scnd.text[0:2]), int(self.scnd.text[4:6]))
    		self.my_thread=threading.Thread(target=self.second_thread)
    		self.my_thread.start()
    	if (self.ONOFF.active)==False:
        	self.touchedS=True
    @mainthread
    def IAgree(self,touch):
        if self.ONOFF.active:
        	self.ONOFF.active=False
        	self.audiobool=True
        	self.popupsi.dismiss()
        	

    @mainthread
    def IDAgree(self,touch):
    	if self.ONOFF.active:
        	self.audiobool=True
        	self.LetsGetActivate()
    @mainthread
    def update_screen_to(self,screenname):
    	self.parent.parent.parent.parent.transition.direction = 'left'
    	self.parent.parent.parent.parent.current = screenname
    def second_thread(self):

        # try:

            self.touchedS=False
            # print(self.TimerSession.count)
            # self.update_label_text(str(self.TimerSession.count//60)+":"+str(self.TimerSession.count%60))
            self.TimerSession.CheckTimeTM()
            while self.TimerSession.count>0:
                self.TimerSession.CheckTimeTM()
                
                if  self.touchedS==True:
                    break
                
                if self.TimerSession.count<=0 :
                  	
                    self.my_call_thread=threading.Thread(target=self.new_call_thread)
                    self.my_call_thread.start()

                    
                    break
                    
                time.sleep(1)
    @mainthread
    def Craete_popup(self):
    	self.popupsi.open()
    	self.sound_loop[2].play()
    def new_call_thread(self):
    	self.Craete_popup()
    	print(self.sound_loop[2].state)
    	self.doAlarm()
    	print(self.sound_loop[2].state)
    	self.audiobool=False
    	while True:
            
            
            if  self.audiobool!=False:
                

                self.sound_loop[2].stop()
                self.sound_loop[2]=SoundLoader.load(self.sound_inst_loop[2])

                break
            time.sleep(1)
    @mainthread
    def doAlarm(self):

        self.sound_loop[2].play()
                    
                
    # def LetsDelete(self, touch):
    # 	self.file=file=open("alarms.txt", "a+")
    # 	print("pussy")
    # 	for line in self.file:
    # 		try:
    # 			print("your index"+self.frst.text[7])
    # 			if self.frst.text[8] == line[7]:
    # 				line =" "
    # 		except IndexError: 
    # 			break

        # self.AlarmSession= AlarmSession = Alarm()
    def inputingprocess(self,mint,sec):
        try:
            if (mint == None):
                raise NoargError(mint)
            if (sec == None) :
                raise NoargError(sec)
            
        except NoargError as e:
            e.popupsi.open()
            stratNone= ICommand()
            return stratNone.execute()
        
        else:
            return self.TimerSession.setTimer(float(mint),float(sec))

# if __name__ == '__main__':
#     MainApp().run()