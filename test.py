# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
import asynckivy as ak


class TestApp(App):

    def build(self):
        return Label(text='Сыыышь???!!!', markup=True, font_size='80sp',
                     outline_width=2,
                     outline_color=get_color_from_hex('#FFFFFF'),
                     color=get_color_from_hex('#000000'),
                     )

    def on_start(self):
        async def animate(label):
            await ak.sleep(2.5)
            while True:
                label.outline_color = get_color_from_hex('#FFFFFF')
                label.text = 'Эй, ты!'
                await ak.sleep(1)
                label.font_size='30sp'

                label.text = 'Да-да ты, перед монитором'
                await ak.sleep(2)
                label.text = 'Ты пидор?'
                await ak.sleep(3)
                label.text = 'Нет????!!!!!'
                await ak.sleep(2)

                label.outline_color = get_color_from_hex('#FF5555')
                label.font_size='50sp'
                label.text = 'Полюбому пидор!'
                
                await ak.sleep(2)

                label.outline_color = get_color_from_hex('#FFFF00')
                label.text = 'Если не пидор, нажми на экран!'
                while True:
                    args, kwargs = await ak.event(label, 'on_touch_down')
                    touch = args[1]
                    if touch.button == 'left':
                        break
        ak.start(animate(self.root))


if __name__ == '__main__':
    TestApp().run()