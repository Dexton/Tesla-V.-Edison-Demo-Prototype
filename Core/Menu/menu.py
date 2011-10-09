import pyglet
from pyglet.window import key

import math

class Menu(pyglet.graphics.Batch):
    """ An abstract class describing the basic functionality
        for menus
    """
    SELECTED_COLOUR = (255, 255, 255, 255)
    DESELECTED_COLOUR = (255, 76, 76, 76)
    TITLE_COLOUR = (255, 255, 255, 255)

    def __init__(self, title, options, window, *args, **kwargs):
        """ Initializes the menu
            title: Title of the menu
            options: A list of strings for the options
            window: The window this menu belongs to
        """
        super(Menu, self).__init__(*args, **kwargs)

        self.window = window

        try:
            self.options
        except AttributeError:
            self.options = options

        try:
            self.option_labels
        except AttributeError:
            self.option_labels = list()

        try:
            self.title
        except AttributeError:
            self.title = title

        self.title_label = pyglet.text.Label(text=self.title,
                                             x=self.window.width/2,
                                             y=self.window.height - 60,
                                             anchor_x='center',
                                             anchor_y='top',
                                             font_size=62,
                                             color=Menu.TITLE_COLOUR,
                                             batch=self)

        y_step = 80
        y_start = self.window.height - 180
        for i, opt in enumerate(self.options):
            option = pyglet.text.Label(text=opt,
                                       x=self.window.width/2,
                                       y=y_start - i*y_step,
                                       anchor_x='center',
                                       anchor_y='top',
                                       font_size=42,
                                       color=Menu.SELECTED_COLOUR if i == 0 else Menu.DESELECTED_COLOUR,
                                       batch=self)
            self.option_labels.append(option)

        self.selected_option = self.options[0]

    def on_key_press(self, symbol, modifiers):
        """ Handles key presses for the menu """

        curr_selected_idx = self.options.index(self.selected_option)
        self.option_labels[curr_selected_idx].color = Menu.DESELECTED_COLOUR

        if symbol == key.UP:
            curr_selected_idx -= 1
        if symbol == key.DOWN:
            curr_selected_idx += 1

        curr_selected_idx = curr_selected_idx % len(self.options)

        self.selected_option = self.options[curr_selected_idx]
        self.option_labels[curr_selected_idx].color = Menu.SELECTED_COLOUR
