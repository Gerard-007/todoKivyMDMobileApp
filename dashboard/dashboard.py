from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout

class DashboardScreen(MDScreen):
    def show_app_name(self):
        return toast("Link to another page")


# class DashboardApp(MDApp):
#     def build(self):
#         return DashboardScreen()


# DashboardApp().run()
