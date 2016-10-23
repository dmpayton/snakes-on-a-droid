from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatterlayout import ScatterLayout

class DemoApp(App):
    def build(self):
        scatter = ScatterLayout()
        label = Label(text='hello, world', font_size=60)
        scatter.add_widget(label)
        return scatter

if __name__ == '__main__':
    DemoApp().run()
