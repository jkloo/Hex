#!/usr/bin/env python

"""Grid module. """

import random

from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (NumericProperty,
                             StringProperty,
                             ObjectProperty,
                             ListProperty)

from tile import FieldTile, GrassTile, SandTile
from character import Player


class Grid(FloatLayout):
    tiles = ListProperty()
    tiles_scale = NumericProperty()
    tiles_x = NumericProperty()
    tiles_y = NumericProperty()
    player = ObjectProperty()

    def build_grid(self, nx, ny, scale):
        self.tiles_x = nx
        self.tiles_y = ny
        self.tiles_scale = scale
        self.tiles = []
        for j in range(ny):
            self.tiles.append([])
            for i in range(nx):
                tileType = random.choice([GrassTile, SandTile])
                tile = tileType(i, j, scale)

                if j == 0:
                    tile._exit['down'] = False
                elif j == (ny - 1):
                    tile._exit['up'] = False

                if i == 0:
                    tile._exit['left'] = False
                elif i == (nx - 1):
                    tile._exit['right'] = False

                self.tiles[j].append(tile)
                self.add_widget(tile)

    def add_player(self, grid_x, grid_y, grid_scale, player=None):
        if player:
            self.player = player
        else:
            self.player = Player(grid_x, grid_y, grid_scale)
        self.add_widget(self.player)
