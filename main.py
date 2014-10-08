#!/usr/bin/env python

"""Main module. """

from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import (NumericProperty,
                             StringProperty,
                             ObjectProperty)

from tile import FieldTile, GrassTile, SandTile
from character import Player


class Grid(FloatLayout):
    tiles_scale = NumericProperty()
    tiles_x = NumericProperty()
    tiles_y = NumericProperty()

    def build_grid(self, nx, ny, scale):
        self.player = Player(1, ny - 2, scale)
        self.tiles_x = nx
        self.tiles_y = ny
        self.tiles_scale = scale
        for j in range(ny):
            for i in range(nx):
                self.add_widget(FieldTile(i, j, scale))
        self.add_widget(self.player)


class HexApp(App):
    game = ObjectProperty()

    def build(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_key_down)
        self.game = Grid(size_hint=(None, None))
        self.game.build_grid(20, 20, 50)
        root = ScrollView(size_hint=(1, 1))
        root.add_widget(self.game)
        return root

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] in ['up', 'down', 'left', 'right']:
            return self.game.player.move(keycode[1], movesteps=5)
        elif keycode[1] == 'escape':
            keyboard.release()
        return True

if __name__ == '__main__':
    HexApp().run()
