from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast

# default screen size...
Window.size = (350, 600)


class SignupScreen(MDScreen):
    def register_user(self):
        return toast('You are working too abi?')

    # def nav_to_login(self):
    #     sm = ScreenManager()
    #     sm.add_widget(LoginScreen())
    #     sm.current="login"


class SignupApp(MDApp):
    def build(self):
        # Theme definictions...
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "800"  # "500"
        return SignupScreen()


if __name__=="__main__":
    SignupApp().run()