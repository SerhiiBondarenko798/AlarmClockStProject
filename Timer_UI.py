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
from kivy.uix.image import Image
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from kivy.uix.recycleview import RecycleView
from kivy.uix.splitter import Splitter
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
Builder.load_string('''
<SelectableLabel>:

    
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
        default_size_hint: 1, None
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
    ''' Эта строчка очень нужна, я говорю именно про эту ЗАКОМЕНЧЕННУЮ СТРОЧКУ, СОТРЁШЬ ЕЁ - НАМ ВСЕМ ГАБЕЛЛА!!!! '''


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
    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        if is_selected:
            dic=rv.data[index]
            print(dic['text'])
        # else:
        #     print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(60)]

# class Timerclock_body(BoxLayout):

#     def __init__(self, **kwargs):
#         super(Timerclock_body, self).__init__(**kwargs)
#         #self.get_time_time=get_time_time='00:00'
#         with self.canvas.before:
#             Color(0, 1, 1, 1)#<-----------------Место для функции смены цвета бэка тамербара
#             Line(circle=(200,375,70),width=1.5 )
#             Label(text=self.get_time_time,font_size=30,color=(0, 1, 1, 1),pos=(150,325))
#     # def get_time_to_timer(self):
#     #     get_time_time=Clock.schelude_interval(,0.5)





class SetTimeTM_body(BoxLayout):

    def __init__(self, **kwargs):
        super(SetTimeTM_body, self).__init__(**kwargs)
        self.scroll_mint=scroll_mint=RV()
        self.scroll_sec=scroll_sec=RV()
        self.add_widget(scroll_mint)
        self.add_widget(scroll_sec)
        with self.canvas.before:
            Color(0, 1, 1, 1)#<-----------------Место для функции смены цвета бэка тамербара
            # Line(circle=(200,375,70),width=1.5 )
            #Label(text='tut dolzgna bit funciya',font_size=30,color=(0, 1, 1, 1),pos=(150,325))





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


        



class MainApp(App):
    def LetsGetStartTimer(self):
        print()

    def build(self):



        Timer_Body=FloatLayout()
        #TimerBody.add_widget(Button(text='hello',font_size=5,size=(50,50),background_color=(1,0,0,1)))
        self.root = root = SetTimeTM_body(size_hint=[.8,.9],pos_hint={'center_x':0.5,'y':.1}, padding=[40,10,40,10])
        Timer_Body.add_widget(root)

        Button_Start= TimerLables(size_hint=[1/6,1],pos_hint={'x': 0.1, 'y': 0})
        Button_Start.img1.source='icons8-circled-play-filled-90.png'
        #Button_Start.btn1.bind(on_release=self.LetsGetStartTimer)

        Button_Pause= TimerLables(size_hint=[1/6,1],pos_hint={'center_x': .5, 'y': 0})
        Button_Pause.img1.source='icons8-pause-button-filled-96.png'
        #Button_Pause.btn1.bind(on_release=self.GoTOTimer_widget)

        Button_Stop= TimerLables(size_hint=[1/6,1],pos_hint={'right': 0.9, 'y': 0})
        Button_Stop.img1.source='icons8-no-96.png'
        #Button_Stop.btn1.bind(on_release=self.GoTOTimer_widget)
        Timer_ToolBar=FloatLayout(size_hint=(1,.1))
        Timer_ToolBar.add_widget(Button_Start)
        Timer_ToolBar.add_widget(Button_Pause)
        Timer_ToolBar.add_widget(Button_Stop)
        Timer_Body.add_widget(Timer_ToolBar)
        #TimerBody.add_widget(Button(text='hello',font_size=5,size=(50,50),background_color=(1,0,0,1)))
        return Timer_Body

    

if __name__ == '__main__':
    MainApp().run()