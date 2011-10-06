import pyglet

class GameStates:
    MAIN_MENU = 0
    PLAYING = 1
    PAUSED = 2
    GAME_OVER = 3

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        """ Creates necesary items and displays the menu """
        super(GameWindow, self).__init__(1024, 768, *args, **kwargs)

        self.game_state = GameStates.MAIN_MENU

        self.init_menu_items()

        # this next line makes pyglet call self.update at 120Hz
        # this has to be the last line in __init__
        pyglet.clock.schedule_interval(self.update, 1/120.0)

    def update(self, dt):
        """ Update game information
            dt: time delta, the change in time
        """

    def on_key_press(self, symbol, modifiers):
        """ Key Press Event Handler
            symbol: the symbol(key) pressed
            modifiers: the extra keys pressed (ex. Ctrl or Alt)
        """
        pass

    def on_draw(self):
        """ Draw Screen Event Handler """
        self.clear()

        if self.game_state == GameStates.MAIN_MENU:
            self.main_menu_batch.draw()

    def init_menu_items(self):
        """ Initializes menu items """
        # TODO: Write a class that inherits pyglet.graphics.Batch and defines the behaviour of the main menu
        self.main_menu_batch = pyglet.graphics.Batch()

        title_label = pyglet.text.Label(text='Tesla vs. Edison',
                                        x=1024/2, y=768,
                                        anchor_x='center',
                                        anchor_y='top',
                                        font_size=62,
                                        color=(255, 255, 255, 255),
                                        batch=self.main_menu_batch)

        self.main_menu_options = ['New Game', 'End Screen', 'Exit']

        y_step = 80
        y_start = 768/2 + y_step
        for i, opt in enumerate(self.main_menu_options):
            color = (255, 76, 76, 76)
            if i == 0:
                color = (255, 255, 255, 255)
            option = pyglet.text.Label(text=opt,
                                       x=1024/2,
                                       y=y_start - i*y_step,
                                       anchor_x='center',
                                       anchor_y='top',
                                       font_size=42,
                                       color=color,
                                       batch=self.main_menu_batch)

