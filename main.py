#!/usr/bin/env python

"""Main module. """

from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
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

    def build_grid(self, nx, ny, scale):
        self.player = Player(1, ny - 2, scale)
        self.tiles_x = nx
        self.tiles_y = ny
        self.tiles_scale = scale
        self.tiles = []
        for j in range(ny):
            self.tiles.append([])
            for i in range(nx):
                tile = FieldTile(i, j, scale)

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
        self.add_widget(self.player)


class HexApp(App):
    game = ObjectProperty()
    camera = ObjectProperty()

    def build(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_key_down)
        self.game = Grid(size_hint=(None, None))
        self.game.build_grid(20, 20, 50)
        self.camera = ScrollView(size_hint=(1, 1))
        self.camera.add_widget(self.game)
        return self.camera

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] in ['up', 'down', 'left', 'right']:
            return self.game.player.action(keycode[1], movesteps=10)
        elif keycode[1] == 'escape':
            keyboard.release()
        return True

if __name__ == '__main__':
    HexApp().run()
