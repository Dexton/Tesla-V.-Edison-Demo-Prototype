import pyglet

from game_batch import GameBatch

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

        #self.main_menu_batch = MainMenu(self, self.width, self.height)
        #self.pause_menu_batch = PauseMenu(self, self.width, self.height)

        self.game_batch = GameBatch(self, self.width, self.height)

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

        if self.game_state == GameStates.MAIN_MENU:
            self.main_menu_batch.on_key_press(symbol, modifiers)

        if self.game_state == GameStates.PLAYING:
            self.game_batch.on_key_press(symbol, modifiers)

        if self.game_state == GameStates.PAUSED:
            self.pause_menu_batch.on_key_press(symbol, modifiers)

    def on_draw(self):
        """ Draw Screen Event Handler """
        self.clear()

        if self.game_state == GameStates.MAIN_MENU:
            self.main_menu_batch.draw()
        if self.game_state == GameStates.PLAYING:
            self.game_batch.draw()
        if self.game_state == GameStates.PAUSED:
            self.pause_menu_batch.draw()

