#!/usr/bin/env python

"""Tile module. """

import os
import random

from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty,
                             StringProperty)



class _Tile(Widget):
    _sources = []
    _weights = []
    grid_x = NumericProperty(0)
    grid_y = NumericProperty(0)
    scale = NumericProperty(25)
    source = StringProperty()

    def __init__(self, grid_x, grid_y, scale, *args, **kwargs):
        self.scale = scale
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.source = random.choice(self._sources)
        kwargs['size_hint'] = (None, None)
        super(Tile, self).__init__(*args, **kwargs)


class GrassTile(_Tile):
    _sources = [os.path.join('assets', 'tuxemon', 'grass', 'one.png'),
                os.path.join('assets', 'tuxemon', 'grass', 'two.png')]
    _weights = [50, 50]


class FlowerTile(_Tile):
    _sources = [os.path.join('assets', 'tuxemon', 'grass', 'flower', 'red', 'one.png'),
                os.path.join('assets', 'tuxemon', 'grass', 'flower', 'red', 'two.png'),
                os.path.join('assets', 'tuxemon', 'grass', 'flower', 'red', 'three.png'),
                os.path.join('assets', 'tuxemon', 'grass', 'flower', 'blue', 'one.png'),
                os.path.join('assets', 'tuxemon', 'grass', 'flower', 'blue', 'two.png'),
                os.path.join('assets', 'tuxemon', 'grass', 'flower', 'blue', 'three.png'),
                os.path.join('assets', 'tuxemon', 'grass', 'flower', 'yellow', 'one.png'),
                os.path.join('assets', 'tuxemon', 'grass', 'flower', 'yellow', 'two.png'),
                os.path.join('assets', 'tuxemon', 'grass', 'flower', 'yellow', 'three.png')]
    _weights = []


class FieldTile(_Tile):
    _sources = FlowerTile._sources + GrassTile._sources

