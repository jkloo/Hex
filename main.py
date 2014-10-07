#!/usr/bin/env python

"""Main module. """

from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty,
                             StringProperty)

from tile import FieldTile, GrassTile, SandTile
from player import Player


class Grid(FloatLayout):
    tiles_scale = NumericProperty()
    tiles_x = NumericProperty()
    tiles_y = NumericProperty()

    def build_grid(self, nx, ny, scale):
        self.player = Player(1, 1, scale)
        self.tiles_x = nx
        self.tiles_y = ny
        self.tiles_scale = scale
        for j in range(ny):
            for i in range(nx):
                self.add_widget(FieldTile(i, j, scale))
        self.add_widget(self.player)


class HexApp(App):
    def build(self):
        game = Grid(size_hint=(None, None))
        game.build_grid(100, 100, 64)
        root = ScrollView(size_hint=(1, 1))
        root.add_widget(game)
        return root


if __name__ == '__main__':
    HexApp().run()
