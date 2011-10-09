import pyglet
from pyglet.window import key

from menu import Menu
from .. import game

class Pause(Menu):
    """ A batch of graphics handling the main menu stuffs
        Also handles key presses etc.
    """

    def __init__(self, window, *args, **kwargs):
        """ Initializes menu items """

        title = 'Game Paused'
        options = ['Resume', 'Main Menu', 'Exit']

        super(Pause, self).__init__(title, options, window, *args, **kwargs)

    def on_key_press(self, symbol, modifiers):
        """ Handles key presses for the menu """

        if symbol == key.ENTER:
            curr_selected_idx = self.options.index(self.selected_option)
            self.option_labels[curr_selected_idx].color = Pause.DESELECTED_COLOUR

            if self.selected_option == 'Exit':
                pyglet.app.exit()
            if self.selected_option == 'Resume':
                self.window.game_state = game.GameStates.PLAYING
            if self.selected_option == 'Main Menu':
                self.window.game_state = game.GameStates.MAIN_MENU

            self.selected_option = self.options[0]
            self.option_labels[0].color = Pause.DESELECTED_COLOUR
            return
        else:
            super(Pause, self).on_key_press(symbol, modifiers)
