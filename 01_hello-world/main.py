from kivy.app import App
from kivy.uix.label import Label

class DemoApp(App):
    def build(self):
        return Label(text='hello, world', font_size=60)

if __name__ == '__main__':
    DemoApp().run()
