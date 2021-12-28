from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from login.login import LoginScreen
from signup.signup import SignupScreen
from loading_screen.splash import PreSplashScreen
from dashboard.dashboard import DashboardScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
import requests
import json


Window.size = (350, 600)


class TodoApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "800"
        Builder.load_file("loading_screen/splash.kv")
        Builder.load_file("login/login.kv")
        Builder.load_file("signup/signup.kv")
        Builder.load_file("dashboard/dashboard.kv")
        global sm
        sm = ScreenManager()
        sm.add_widget(PreSplashScreen(name='splash_screen'))
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(SignupScreen(name='signup_screen'))
        sm.add_widget(DashboardScreen(name='dashboard_screen'))
        return sm

    def on_start(self):
        Clock.schedule_once(self.login, 5)

    def login(self, *args):
        sm.current = "login_screen"


if __name__ == "__main__":
    TodoApp().run()