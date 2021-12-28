import importlib
import os
from kaki.app import App
from kivy.core.window import Window
from kivy.factory import Factory
from kivymd.app import MDApp
from dashboard import DashboardApp

Window.size=(350, 600)

class MDLive(App, DashboardApp):
    DEBUG = 1
    KV_FILES = (
        os.path.join(os.getcwd(), "dashboard/dashboard.kv"),
    )
    CLASSES = {
        "DashboardScreen": "dashboard"
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]
    def build_app(self, *args):
        print("Inside Build App Auto Just Reloaded")
        return Factory.DashboardScreen()

MDLive().run()
