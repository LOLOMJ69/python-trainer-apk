from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0, 0, 0, 1)

class MyApp(App):
    def build(self):
        return Label(
            text="Python Trainer APK 😈",
            color=(0, 1, 0.5, 1),
            font_size="28sp"
        )

MyApp().run()
