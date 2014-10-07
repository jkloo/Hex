#!/usr/bin/env python

"""Player module. """

from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty,
                             StringProperty)

class Player(Widget):
    grid_x = NumericProperty(0)
    grid_y = NumericProperty(0)
    grid_scale = NumericProperty(25)
    source = StringProperty()
    def __init__(self, grid_x, grid_y, grid_scale, *args, **kwargs):
        self.source = 'assets/characters/hero.png'
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.grid_scale = grid_scale
        kwargs['size_hint'] = (None, None)
        super(Player, self).__init__(*args, **kwargs)
