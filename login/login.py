from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivymd.uix.floatlayout import MDFloatLayout
import requests
import json

# default screen size...
Window.size = (350, 600)

class LoginScreen(MDScreen):
    def authenticate_user(self):
        self.manager.current = 'dashboard_screen'

        #___Api Calls here with authentication already working...
        '''
            url = "https://todoresapi.herokuapp.com/api/auth/login"

            payload = json.dumps({
                "email": self.ids.user_email.text,
                "password": self.ids.user_password.text,
            })
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            login_response = response.json()
            print(login_response)
            if response.status_code == 200:
                global user_token
                user_token = login_response["token"]
                toast(f'Welcome {login_response["email"]}')
                # Switch screens here...
                self.manager.current = 'dashboard_screen'
            else:
                toast(f'{login_response["message"]}')
        '''


# class LoginApp(MDApp):
#     def __init__(self, *args):
#         super(LoginApp, self).__init__(*args)

#     def build(self):
#         return LoginScreen()


# LoginApp().run()


# class AuthUserApp(MDApp):
#     def build(self):
#         # Theme definictions...
#         self.theme_cls.primary_palette = "Indigo"
#         self.theme_cls.primary_hue = "800"  # "500"
#         global sm
#         sm = ScreenManager()
#         sm.add_widget(PreSplashScreen(name='pre_splash'))
#         sm.add_widget(LoginScreen(name='login'))
#         sm.add_widget(SignupScreen(name='signup'))
#         return sm

#     def on_start(self):
#         Clock.schedule_once(self.login, 5)

#     def login(self, *args):
#         sm.current = "login"


# if __name__=="__main__":
#     AuthUserApp().run()