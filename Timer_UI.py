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
import time
import types
from Time import Time 
from Timer import Timer
Builder.load_string('''
<TimerClockLab>:
    font_size: 50
    color: (0, 1, 1, 1)
    canvas:
        
        Color: 
            rgba:(0, 1, 1, 1)#<-----------------Место для функции смены цвета бэка тамербара
        Line:
            circle: (self.center_x,self.center_y,100)
            width: 1.5

<SetTimeTM_body>:
    canvas.before:
        Color:
            rgba:(0, 1, 1, 1)
        

<SelectableLabel>:
    
    font_size: 50
    color: (.1,.1,.1,1) if self.selected else (0,1,1,1)
    canvas.before:
        Color:
            rgba: (0,1,1,1) if self.selected else (0, 0, 0, 0)
        Rectangle:
            pos: self.pos
            size: self.size
<RV>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: .95, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        # multiselect: True
        # touch_multiselect: True
''')



Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 700)
Config.set('graphics', 'resizable', 0)


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,RecycleBoxLayout):
    ''' Эта строчка очень нужна, я говорю именно про эту ЗАКОМЕНЧЕННУЮ СТРОЧКУ, СОТРЁШЬ ЕЁ : НАМ ВСЕМ ГАБЕЛЛА!!!! '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)
    def on_touch_down(self, touch):
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)
        if self.selected:
            self.selected=False
    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        if is_selected:
            dicvalue=rv.data[index]['text']
            if self.parent.parent.id == 'minuteslist':
                self.parent.parent.parent.parent.parent.parent.parent.valueminutes=dicvalue
            elif self.parent.parent.id == 'secondslist':
                self.parent.parent.parent.parent.parent.parent.parent.valueseconds=dicvalue
            is_selected=False
    
           
class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)

        self.data = [{'text': str(x),'keyforacc': str(x)} for x in range(60)]








class TimerClockLab(Label):
   def __init__(self, **kwargs):
        super(TimerClockLab, self).__init__(**kwargs)
        

        

class TimerClock_Body(BoxLayout):

    def __init__(self, **kwargs):
        super(TimerClock_Body, self).__init__(**kwargs)
        # self.get_time_time=get_time_time='00:00'
        self.TM_TC_Label=TM_TC_Label=TimerClockLab(text=' ',pos_hint={'center_x':0.5,'center_y':0.5})
        self.add_widget(TM_TC_Label)
        with self.canvas.before:
            Color(0, 1, 1, 1)#<-----------------Место для функции смены цвета бэка тамербара    
    
class SetTimeTM_body(BoxLayout):

    def __init__(self, **kwargs):
        super(SetTimeTM_body, self).__init__(**kwargs)
        self.scroll_mint=scroll_mint=RV(id='minuteslist',size_hint=(.5,1),pos_hint={'x': 0.0, 'top': 1})
        self.scroll_sec=scroll_sec=RV(id='secondslist',size_hint=(.5,1),pos_hint={'right': 1.0, 'top': 1})
        self.add_widget(scroll_mint)
        self.add_widget(scroll_sec)

        #<-----------------Место для функции смены цвета бэка тамербара

        
class TM_SM(ScreenManager):

    def __init__(self, **kwargs):
        super(TM_SM, self).__init__(**kwargs)
        self.snovadarou=snovadarou=Set_Time_Screen()
        self.add_widget(snovadarou)
        

class Set_Time_Screen(Screen):
    def __init__(self, **kwargs):
        super(Set_Time_Screen, self).__init__(**kwargs)
        self.darou=darou=SetTimeTM_body(size_hint=(1,1),pos_hint={'center_x':0.5,'center_y':0.5},padding =[0,0,0,0])
        self.add_widget(darou)

class Act_Time_Screen(Screen):
    def __init__(self, **kwargs):
        super(Act_Time_Screen, self).__init__(**kwargs)
        self.TMWindow=TMWindow=TimerClock_Body()
        self.add_widget(TMWindow)

class TimerLables(AnchorLayout):
    def __init__(self, **kwargs):
        super(TimerLables, self).__init__(**kwargs)
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



		


class Timer_widget(FloatLayout,I_Button):
    stop = threading.Event()
    def __init__(self, **kwargs):
        super(Timer_widget, self).__init__(**kwargs)
        Timer_Body=FloatLayout(pos_hint={'center_x':0.5,'y':0})
        self.SM_TM = SM_TM  =ScreenManager(size_hint=[1,.8],pos_hint={'center_x':0.5,'top':1})
        self.frst=frst=Set_Time_Screen(name='STS',id='firstw')
        self.scnd=scnd=Act_Time_Screen(name='ATS',id='scndw')
        self.SM_TM.add_widget(frst)
        self.SM_TM.add_widget(scnd)
        self.TimerSession= TimerSession = Timer()

        Button_Start= TimerLables(size_hint=[1/5.5,1],pos_hint={'x': 0.1, 'y': 0})
        Button_Start.img1.source='icons8-circled-play-filled-90.png'
        Button_Start.btn1.bind(on_release=self.LetsGetStart)

        Button_Pause= TimerLables(size_hint=[1/5.5,1],pos_hint={'center_x': .5, 'y': 0})
        Button_Pause.img1.source='icons8-pause-button-filled-96.png'
        Button_Pause.btn1.bind(on_release=self.LetsGetPause)

        Button_Stop= TimerLables(size_hint=[1/5.5,1],pos_hint={'right': 0.9, 'y': 0})
        Button_Stop.img1.source='icons8-no-96.png'
        Button_Stop.btn1.bind(on_release=self.LetsGetStop)
        self.valueseconds = None
        self.valueminutes = None


        Timer_ToolBar=FloatLayout(size_hint=(.9,.1),pos_hint={'center_x':0.5,'y':0})
        Timer_ToolBar.add_widget(Button_Start)
        Timer_ToolBar.add_widget(Button_Pause)
        Timer_ToolBar.add_widget(Button_Stop)




        Timer_Body.add_widget(SM_TM)
        Timer_Body.add_widget(Timer_ToolBar)
        self.add_widget(Timer_Body)

    def LetsGetStart(self, touch):
        if self.SM_TM.children[0].id == 'firstw':

            strat = CommandInputed(self.inputingprocess)
            strat.execute(self, self.valueminutes, self.valueseconds)
            # self.inputingprocess(self.valueminutes,self.valueseconds)
        self.SM_TM.transition.direction = 'left'
        self.SM_TM.current = 'ATS'
        threading.Thread(target=self.second_thread, args=(self.SM_TM.children[0].TMWindow.TM_TC_Label.text,)).start() 
           
      
        # else:  
        #     self.SM_TM.transition.direction = 'left'
        #     self.SM_TM.current = 'ATS'
    @mainthread
    def update_label_text(self,new_text):
        self.SM_TM.children[0].TMWindow.TM_TC_Label.text=new_text


    def second_thread(self,l_text):

        try:
            while True:
                if self.TimerSession.count<0: 
                    self.update_label_text("00:00")
                    break
                Clock.schedule_once(self.TimerSession.CheckTimeTM, 0)
                self.update_label_text(str(int(self.TimerSession.count//60))+":"+str(int(self.TimerSession.count%60)))
                time.sleep(1)
                
        except AttributeError:
            self.SM_TM.transition.direction = 'right'
            self.SM_TM.current = 'STS'


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
    def LetsGetPause(self,touch):
        pass
    def LetsGetStop(self,touch):
        self.SM_TM.transition.direction = 'right'
        self.SM_TM.current = 'STS'
        # self.TimerSession.StopTM(True)
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


class countZero(Exception):
    def __init__(self, value):
        super(countZero, self).__init__()
        self.value = value        

class NoargError(Exception):
    def __init__(self, value):
        super(NoargError, self).__init__()
        self.value = value
        self.popupsi=Popup(title='Unexpected/uninputed value',content=Label(text="\nHi,maybe you entered the wrong value\n or forgot to enter it at all\n,lets see what you entered:\n You entered:{0} but this value changed to 0".format(value)),size_hint=(1, .9))
        
class MainApp(App):
	def build(self):
		return Timer_widget()



if __name__ == '__main__':
    MainApp().run()
