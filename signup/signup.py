from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
import requests
import json


# default screen size...
Window.size = (350, 600)

Builder.load_file("signup/signup.kv")


class SignupScreen(MDScreen):

    def register_user(self):
        self.manager.current = 'login_screen'

        '''
            #___Api Calls here with authentication already working...

            url = "https://todoresapi.herokuapp.com/api/auth/register"

            payload = json.dumps({
                "username": self.ids.username_field.text,
                "email": self.ids.email_field.text,
                "password": self.ids.password_field.text,
            })
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            signup_response = response.json()
            print(signup_response)
            print(response.status_code)
            if response.status_code==201:
                print(response.text)
                print(response.status_code)
                toast(f"user: {signup_response['username']} created succesfully")
                self.manager.current = "login_screen"
            elif signup_response["username"]:
                toast(f"{signup_response['username']}")
            else:
                toast("Wrong input")
        '''


#___ For testing purposes...
# class SignupApp(MDApp):
#     def __init__(self, *args):
#         super(SignupApp, self).__init__(*args)

#     def build(self):
#         return SignupScreen()

# SignupApp().run()