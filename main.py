
import os
import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty,
                             StringProperty,
                             ReferenceListProperty,
                             ObjectProperty)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.atlas import Atlas

class Tile(Widget):
    grid_x = NumericProperty(0)
    grid_y = NumericProperty(0)
    scale = NumericProperty(25)
    source = StringProperty()

    @staticmethod
    def new_tile(grid_x, grid_y, scale, source):
        tile = Tile()
        tile.scale = scale
        tile.grid_x = grid_x
        tile.grid_y = grid_y
        tile.source = source
        return tile


class Grid(Widget):
    def build_grid(self, nx, ny):
        for j in range(ny):
            for i in range(nx):
                source = 'assets/tuxemon/tuxemon-{j}-{i}.png'.format(j=j, i=i)
                self.add_widget(Tile.new_tile(i, j, 50, source))


class HexApp(App):
    def build(self):
        game = Grid()
        game.build_grid(10, 10)
        return game


if __name__ == '__main__':
    HexApp().run()
