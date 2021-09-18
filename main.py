from kivy.factory import Factory
from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

# default screen size...
Window.size = (350, 600)

class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "800"  # "500"
        return Builder.load_file("main.kv")

    def rail_open(self):
        if self.root.ids.rail.rail_state == "open":
            self.root.ids.rail.rail_state = "close"
        else:
            self.root.ids.rail.rail_state = "open"

    # def on_start(self):
    #     for _ in range(9):
    #         tile = Factory.MyTile(source="kitten.png")
    #         tile.stars = 5
    #         self.root.ids.box.add_widget(tile)


Test().run()