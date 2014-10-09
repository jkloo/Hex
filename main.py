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

from grid import Grid
import settings
import keymap

class HexApp(App):
    game = ObjectProperty()
    camera = ObjectProperty()

    def build(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed,
                                                 self,
                                                 'text')
        self._keyboard.bind(on_key_down=self._on_key_down)

        self.game = Grid(size_hint=(None, None))
        self.game.build_grid(settings.GRID_WIDTH,
                             settings.GRID_HEIGHT,
                             settings.GRID_SCALE)
        self.game.add_player(0,
                             settings.GRID_HEIGHT - 1,
                             settings.GRID_SCALE)

        self.camera = ScrollView(size_hint=(1, 1))
        self.camera.add_widget(self.game)

        return self.camera

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] in keymap.WALK_DIRECTIONS:
            return self.game.player.action(keycode[1],
                                           movesteps=settings.MOVE_STEPS)
        elif keycode[1] == keymap.QUIT:
            keyboard.release()
        return True

if __name__ == '__main__':
    HexApp().run()
