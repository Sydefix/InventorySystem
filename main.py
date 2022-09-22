
# from kivy.app  import  App
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# from kivy.core.window import Window
# from kivy.uix.button import Button

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.label import label
from kivy.uix.widget import Widget
from kivy.core.window import Window

# Window.clearcolor = (1,1,1,1)
Window.size = (360,600)

class demo(MDApp):
    def build(self):
        return super().build()

        

demo().run()

