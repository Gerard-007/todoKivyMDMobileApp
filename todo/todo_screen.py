import datetime
from datetime import date

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen

Window.size = (350, 600)


class TodoCard(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class TodoScreen(MDScreen):
    pass


class TodoApp(MDApp):
    def build(self):
        # Theme definictions...
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "800"  # "500"
        global sm
        sm=ScreenManager()
        sm.add_widget(TodoScreen())
        return sm

    def on_start(self):
        today = date.today()
        wd = date.weekday(today)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().strftime("%b"))
        day = str(datetime.datetime.now().strftime("%d"))
        sm.get_screen("todo_list").date.text=f'{days[wd]}, {day} {month} {year}'

if __name__ == "__main__":
    TodoApp().run()
