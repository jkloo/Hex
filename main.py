from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class Tile(Widget):
    pass


class Row(Widget):
    tile_width = NumericProperty()


class Grid(Widget):
    pass


class HexApp(App):
    def build(self):
        game = Grid()
        return game


if __name__ == '__main__':
    HexApp().run()
