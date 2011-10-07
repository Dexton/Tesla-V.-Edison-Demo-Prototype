import pyglet
from pyglet.window import key

import game
from pause_menu import PauseMenu

class GameBatch(pyglet.graphics.Batch):
    """ The batch of game graphics, also handles the updates of the positions etc. """

    # TODO: Move the pause menu to the game window for easier handling

    def __init__(self, window, width, height, *args, **kwargs):
        """ Initializes menu items """
        super(GameBatch, self).__init__(*args, **kwargs)

        self.window = window

        self.pause_batch = PauseMenu(self.window, width, height)

    # Override the draw function to include the pause menu
    def draw(self):
        super(GameBatch, self).draw()

        if self.window.game_state == game.GameStates.PAUSED:
            self.pause_batch.draw()

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
        print symbol

        if symbol == key.ESCAPE:
            self.window.game_state == game.GameStates.PAUSED

