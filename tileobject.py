#!/usr/bin/env python

"""TileObject module. """

from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty,
                             StringProperty)


class TileObject(Widget):
    grid_x = NumericProperty(0)
    grid_y = NumericProperty(0)
    grid_scale = NumericProperty(25)
    _sources = []
    _actions = {'U': None, 'D': None, 'L': None, 'R': None}  # action handlers. local (x, y, direction)

    def __init__(self, grid_x, grid_y, grid_scale, *args, **kwargs):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.grid_scale = grid_scale
        kwargs['size_hint'] = (None, None)
        super(TileObject, self).__init__(*args, **kwargs)

class MultiTileObject(Widget):
    grid_x = NumericProperty(0)
    grid_y = NumericProperty(0)
    grid_scale = NumericProperty(25)
    grid_height = NumericProperty(1)
    grid_width = NumericProperty(1)

    _objects = []

    def __init__(self, grid_x, grid_y, grid_height,
                 grid_width, grid_scale, *args, **kwargs):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid_scale = grid_scale
        kwargs['size_hint'] = (None, None)
        super(TileObject, self).__init__(*args, **kwargs)
