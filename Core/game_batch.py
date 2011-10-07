import pyglet
from pyglet.window import key

import game
from pause_menu import PauseMenu

class GameBatch(pyglet.graphics.Batch):
    """ The batch of game graphics, also handles the updates of the positions etc. """

    def __init__(self, window, width, height, *args, **kwargs):
        """ Initializes menu items """
        super(GameBatch, self).__init__(*args, **kwargs)

        self.window = window

    def update(self, dt):
        """ Update game information
            dt: time delta, the change in time
        """

    def on_key_press(self, symbol, modifiers):
        """ Key press event handler
            symbol: the symbol(key) pressed
            modifiers: the extra keys pressed (ex. Ctrl or Alt)

            Called by the on_key_press function in the GameWindow class
        """
        if symbol == key.ESCAPE:
            self.window.game_state = game.GameStates.PAUSED

