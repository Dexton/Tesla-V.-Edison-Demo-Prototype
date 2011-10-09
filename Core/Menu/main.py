import pyglet
from pyglet.window import key

from menu import Menu
from .. import game

class Main(Menu):
    """ A batch of graphics handling the main menu stuffs
        Also handles key presses etc.
    """

    def __init__(self, window, *args, **kwargs):
        """ Initializes menu items """

        title = 'Tesla v. Edison'
        options = ['New Game', 'End Screen', 'Exit']

        super(Main, self).__init__(title, options, window, *args, **kwargs)

    def on_key_press(self, symbol, modifiers):
        """ Handles key presses for the menu """

        if symbol == key.ENTER:
            curr_selected_idx = self.options.index(self.selected_option)
            self.option_labels[curr_selected_idx].color = Main.DESELECTED_COLOUR

            if self.selected_option == 'Exit':
                pyglet.app.exit()
            if self.selected_option == 'New Game':
                self.window.game_state = game.GameStates.PLAYING
            if self.selected_option == 'End Screen':
                self.window.game_state = game.GameStates.GAME_OVER

            self.selected_option = self.options[0]
            self.option_labels[0].color = Main.DESELECTED_COLOUR
            return
        else:
            super(Main, self).on_key_press(symbol, modifiers)
