#!/usr/bin/env python

"""Tile module. """

import os
import random

from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty,
                             StringProperty,
                             DictProperty)

from config import ASSETS_DIR


class Tile(Widget):
    _sources = []
    _entry = DictProperty({'up': True, 'down': True, 'left': True, 'right': True})
    _exit = DictProperty({'up': True, 'down': True, 'left': True, 'right': True})
    grid_x = NumericProperty(0)
    grid_y = NumericProperty(0)
    grid_scale = NumericProperty(25)
    source = StringProperty()

    def __init__(self, grid_x, grid_y, grid_scale, *args, **kwargs):
        self.grid_scale = grid_scale
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.source = random.choice(self._sources)
        kwargs['size_hint'] = (None, None)
        super(Tile, self).__init__(*args, **kwargs)

    def enter(self, direction):
        return self._entry.get(direction, False)

    def exit(self, direction):
        return self._exit.get(direction, True)

    def neighbor(self, direction):
        n = [0, 0]
        if direction == 'left':
            n = [-1, 0]
        elif direction == 'right':
            n = [1, 0]
        elif direction == 'up':
            n = [0, 1]
        elif direction == 'down':
            n = [0, -1]
        new_x = self.grid_x + n[0]
        new_y = self.grid_y + n[1]
        try:
            new_tile = self.parent.tiles[new_y][new_x]
        except IndexError:
            new_tile = None
        finally:
            return new_tile



class GrassTile(Tile):
    _sources = [os.path.join(ASSETS_DIR, 'tiles', 'grass', 'one.png'),
                os.path.join(ASSETS_DIR, 'tiles', 'grass', 'two.png')]
    _entry = {'up': False, 'down': False, 'left': False, 'right': False}


class SandTile(Tile):
    _sources = [os.path.join(ASSETS_DIR, 'tiles', 'sand', 'one.png'),
                os.path.join(ASSETS_DIR, 'tiles', 'sand', 'two.png')]


class FlowerTile(Tile):
    _sources = [os.path.join(ASSETS_DIR, 'tiles', 'grass', 'flower', 'red', 'one.png'),
                os.path.join(ASSETS_DIR, 'tiles', 'grass', 'flower', 'red', 'two.png'),
                os.path.join(ASSETS_DIR, 'tiles', 'grass', 'flower', 'red', 'three.png'),
                os.path.join(ASSETS_DIR, 'tiles', 'grass', 'flower', 'blue', 'one.png'),
                os.path.join(ASSETS_DIR, 'tiles', 'grass', 'flower', 'blue', 'two.png'),
                os.path.join(ASSETS_DIR, 'tiles', 'grass', 'flower', 'blue', 'three.png'),
                os.path.join(ASSETS_DIR, 'tiles', 'grass', 'flower', 'yellow', 'one.png'),
                os.path.join(ASSETS_DIR, 'tiles', 'grass', 'flower', 'yellow', 'two.png'),
                os.path.join(ASSETS_DIR, 'tiles', 'grass', 'flower', 'yellow', 'three.png')]


class FieldTile(Tile):
    _sources = FlowerTile._sources + GrassTile._sources
