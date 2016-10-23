from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

class DemoApp(App):
    def build(self):
        layout = FloatLayout()
        open_button = Button(
            text='click me!',
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        layout.add_widget(open_button)

        popup = Popup(
            title='hello, world',
            auto_dismiss=False,
            size_hint=(.3, .3)
        )
        close_button = Button(text='close me!')
        popup.add_widget(close_button)

        open_button.bind(on_release=popup.open)
        close_button.bind(on_release=popup.dismiss)

        return layout

if __name__ == '__main__':
    DemoApp().run()
