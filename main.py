
import os
import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import (NumericProperty,
                             StringProperty)


class Tile(Widget):
    grid_x = NumericProperty(0)
    grid_y = NumericProperty(0)
    scale = NumericProperty(25)
    source = StringProperty()

    @staticmethod
    def new_tile(grid_x, grid_y, scale, source):
        tile = Tile(size_hint=(None, None))
        tile.scale = scale
        tile.grid_x = grid_x
        tile.grid_y = grid_y
        tile.source = source
        return tile


class Grid(FloatLayout):
    tiles_scale = NumericProperty()
    tiles_x = NumericProperty()
    tiles_y = NumericProperty()

    def build_grid(self, nx, ny, scale):
        self.tiles_x = nx
        self.tiles_y = ny
        self.tiles_scale = scale
        for j in range(ny):
            for i in range(nx):
                y = random.randint(0,12)
                x = random.randint(0,7)
                source = 'assets/tuxemon/tuxemon-{}-{}.png'.format(y, x)
                self.add_widget(Tile.new_tile(i, j, scale, source))


class HexApp(App):
    def build(self):
        game = Grid(size_hint=(None, None))
        game.build_grid(100, 100, 32)
        root = ScrollView(size_hint=(1, 1))
        root.add_widget(game)
        return root


if __name__ == '__main__':
    HexApp().run()
