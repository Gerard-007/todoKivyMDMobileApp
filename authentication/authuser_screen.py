from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast

# default screen size...
Window.size = (350, 600)


class PreSplashScreen(MDScreen):
    pass


class LoginScreen(MDScreen):
    def authenticate_user(self):
        return toast('You are workin abi?')
        # user = self.ids.username_field.text
        # pwd = self.ids.pwd_field.text
        # if user:
        #     self.root.ids.auth_user.add_widget(on_press=root.manager.current="dashboard")
        # toast('Invalid login credentials...'


class SignupScreen(MDScreen):
    def register_user(self):
        return toast('You are working too abi?')


class AuthUserApp(MDApp):
    def build(self):
        # Theme definictions...
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "800"  # "500"
        global sm
        sm = ScreenManager()
        sm.add_widget(PreSplashScreen(name='pre_splash'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        return sm

    def on_start(self):
        Clock.schedule_once(self.login, 5)

    def login(self, *args):
        sm.current = "login"


if __name__=="__main__":
    AuthUserApp().run()