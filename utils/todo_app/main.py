import importlib
import os
from kaki.app import App
from kivy.core.window import Window
from kivy.factory import Factory
from kivymd.app import MDApp
from todo import TodoApp

Window.size=(350, 600)

class MDLive(App, TodoApp):
    DEBUG = 1
    KV_FILES = (
        os.path.join(os.getcwd(), "todo_app/todo.kv"),
    )
    CLASSES = {
        "TodoScreen": "todo"
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]
    def build_app(self, *args):
        print("Todo App Auto Just Reloaded")
        return Factory.TodoScreen()

MDLive().run()
