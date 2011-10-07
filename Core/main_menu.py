import pyglet
from pyglet.window import key

import math

import game

class MainMenu(pyglet.graphics.Batch):
    """ A batch of graphics handling the main menu stuffs
        Also handles key presses etc.
    """
    SELECTED_COLOR = (255, 255, 255, 255)
    DESELECTED_COLOR = (255, 76, 76, 76)

    def __init__(self, window, width, height, *args, **kwargs):
        """ Initializes menu items """
        super(MainMenu, self).__init__(*args, **kwargs)

        self.window = window

        self.options = ['New Game', 'End Screen', 'Exit']
        self.option_labels = list()

        self.title = pyglet.text.Label(text='Tesla vs. Edison',
                                       x=width/2, y=height - 120,
                                       anchor_x='center',
                                       anchor_y='top',
                                       font_size=62,
                                       color=(255, 255, 255, 255),
                                       batch=self)

        y_step = 80
        y_start = height/math.ceil(len(self.options)/2.0) + y_step
        for i, opt in enumerate(self.options):
            color = MainMenu.DESELECTED_COLOR
            if i == 0:
                color = MainMenu.SELECTED_COLOR
            option = pyglet.text.Label(text=opt,
                                       x=width/2,
                                       y=y_start - i*y_step,
                                       anchor_x='center',
                                       anchor_y='top',
                                       font_size=42,
                                       color=color,
                                       batch=self)
            self.option_labels.append(option)

        self.selected_option = self.options[0]

    def on_key_press(self, symbol, modifiers):
        """ Handles key presses for the menu """

        if symbol == key.ENTER:
            if self.selected_option == 'Exit':
                pyglet.app.exit()
                return
            if self.selected_option == 'New Game':
                self.window.game_state = game.GameStates.PLAYING
                return
            if self.selected_option == 'End Screen':
                self.window.game_state = game.GameStates.GAME_OVER

        curr_selected_idx = self.options.index(self.selected_option)
        self.option_labels[curr_selected_idx].color = MainMenu.DESELECTED_COLOR

        if symbol == key.UP:
            curr_selected_idx -= 1

        if symbol == key.DOWN:
            curr_selected_idx += 1

        curr_selected_idx = curr_selected_idx % len(self.options)

        self.selected_option = self.options[curr_selected_idx]
        self.option_labels[curr_selected_idx].color = MainMenu.SELECTED_COLOR

