#!/usr/bin/env python

"""Character module. """

import random
from functools import partial

from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty,
                             StringProperty,
                             BooleanProperty)

class Character(Widget):
    _animframe = NumericProperty(0)
    _animation = {}
    _animating = BooleanProperty(False)
    _moveframe = NumericProperty(0)
    _moving = BooleanProperty(False)
    grid_x = NumericProperty(0)
    grid_y = NumericProperty(0)
    grid_scale = NumericProperty(25)
    source = StringProperty()
    facing = StringProperty('down')


    def __init__(self, grid_x, grid_y, grid_scale, *args, **kwargs):
        self.grid_scale = grid_scale
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.source = self._animation.get('down')[0]
        kwargs['size_hint'] = (None, None)
        super(Character, self).__init__(*args, **kwargs)

    def move(self, direction, dt=0.3, movesteps=0):
        capture = False
        if direction in ['left', 'right', 'up', 'down'] and not self._animating and not self._moving:
            capture = True
            if self.facing == direction:
                self._animating = True
                self._animframe = len(self._animation.get(direction, []))
                self._moving = True
                self._moveframe = movesteps or self._animframe
                amount = self.grid_scale / self._moveframe
                anim_dt = dt / self._animframe
                move_dt = dt / self._moveframe
                Clock.schedule_once(partial(self._move, direction, amount), move_dt)
                Clock.schedule_once(partial(self._animate, direction), anim_dt)
            else:
                self.source = self._animation.get(direction)[0]
                self.facing = direction
        return capture

    def _move(self, direction, amount, dt):
        self._moveframe -= 1
        if direction == 'left':
            self.x -= amount
            if self._moveframe == 0:
                self.grid_x -= 1
                self._moving = False

        elif direction == 'right':
            self.x += amount
            if self._moveframe == 0:
                self.grid_x += 1
                self._moving = False

        elif direction == 'up':
            self.y += amount
            if self._moveframe == 0:
                self.grid_y += 1
                self._moving = False

        elif direction == 'down':
            self.y -= amount
            if self._moveframe == 0:
                self.grid_y -= 1
                self._moving = False
        if self._moving:
            Clock.schedule_once(partial(self._move, direction, amount), dt)

    def _animate(self, direction, dt):
        self._animframe -= 1
        if self._animframe != 0:
            animlist = self._animation.get(direction)
            self.source = animlist[(animlist.index(self.source) + 1) % (len(animlist))]
            Clock.schedule_once(partial(self._animate, direction), dt)
        else:
            self._animating = False
            self.source = self._animation.get(direction)[0]


class Player(Character):
    _animation = {'up': ['assets/characters/alienGreen.png',
                         'assets/characters/alienPink.png',
                         'assets/characters/alienYellow.png',
                         'assets/characters/alienBeige.png',
                         'assets/characters/alienBlue.png'],
                  'down': ['assets/characters/hero-down-0.png',
                           'assets/characters/hero-down-1.png',
                           'assets/characters/hero-down-2.png',
                           'assets/characters/hero-down-3.png'],
                  'left': ['assets/characters/hero-left-0.png',
                           'assets/characters/alienBeige.png',
                           'assets/characters/alienBlue.png',
                           'assets/characters/alienGreen.png',
                           'assets/characters/alienPink.png'],
                  'right': ['assets/characters/alienBeige.png',
                            'assets/characters/alienBlue.png',
                            'assets/characters/alienGreen.png',
                            'assets/characters/alienPink.png',
                            'assets/characters/alienYellow.png']
                  }
