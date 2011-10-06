import pyglet

class MainMenu(pyglet.graphics.Batch):
    """ A batch of graphics handling the main menu stuffs
        Also handles key presses etc.
    """

    # TODO: Handle key presses etc.

    def __init__(self, width, height, *args, **kwargs):
        """ Initializes menu items """
        super(MainMenu, self).__init__(*args, **kwargs)

        self.title = pyglet.text.Label(text='Tesla vs. Edison',
                                       x=width/2, y=height - 120,
                                       anchor_x='center',
                                       anchor_y='top',
                                       font_size=62,
                                       color=(255, 255, 255, 255),
                                       batch=self)

        self.options = ['New Game', 'End Screen', 'Exit']

        y_step = 80
        y_start = height/2 + y_step
        for i, opt in enumerate(self.options):
            color = (255, 76, 76, 76)
            if i == 0:
                color = (255, 255, 255, 255)
            option = pyglet.text.Label(text=opt,
                                       x=width/2,
                                       y=y_start - i*y_step,
                                       anchor_x='center',
                                       anchor_y='top',
                                       font_size=42,
                                       color=color,
                                       batch=self)

