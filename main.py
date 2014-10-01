
import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty,
                             ReferenceListProperty,
                             ObjectProperty)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.atlas import Atlas

class Tile(Widget):
    pass


class Grid(Widget):
    def build_grid(self, x, y, atlas):
        for j in range(y):
            for i in range(x):
                tile = Tile()
                tile.pos = (i * 100, j * 100)
                key = random.choice(atlas.textures.keys())
                tile.source = atlas[key]
                self.add_widget(tile)



class HexApp(App):
    def build(self):
        self.atlas = Atlas('assets/tuxemon.atlas')
        game = Grid()
        game.build_grid(4, 5, self.atlas)
        return game


if __name__ == '__main__':
    HexApp().run()
