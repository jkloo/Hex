#!/usr/bin/env python

"""Character module. """

import random

from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty,
                             StringProperty)

class Character(Widget):
    _sources = []
    grid_x = NumericProperty(0)
    grid_y = NumericProperty(0)
    grid_scale = NumericProperty(25)
    source = StringProperty()
    facing = StringProperty('D')

    def __init__(self, grid_x, grid_y, grid_scale, *args, **kwargs):
        self.grid_scale = grid_scale
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.source = random.choice(self._sources)
        kwargs['size_hint'] = (None, None)
        super(Character, self).__init__(*args, **kwargs)

    def move(self, direction, amount=1, dt=0.2):
        capture = True
        if direction == 'left':
            self.grid_x -= amount
        elif direction == 'right':
            self.grid_x += amount
        elif direction == 'up':
            self.grid_y += amount
        elif direction == 'down':
            self.grid_y -= amount
        else:
            capture = False
        return capture


class Player(Character):
    _animate = {'U': [], 'D': [], 'L': [], 'R': []}
    _sources = ['assets/characters/hero.png']
