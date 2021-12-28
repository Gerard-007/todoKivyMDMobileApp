from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout


# default screen size...
Window.size = (350, 600)


class PreSplashScreen(MDScreen):
    pass


# class SplashApp(MDApp):

#     def build(self):
#         return PreSplashScreen()


# SplashApp().run()

