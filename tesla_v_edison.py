import pyglet

class GameStates:
    MAIN_MENU = 0
    PLAYING = 1
    PAUSED = 2
    GAME_OVER = 3
    TOP_SCORES = 4

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(800, 600, *args, **kwargs)

        # I have to create a screen, the screen is gotten from pyglet.window.Display using the functions get_screens() or get_default_screen()
        # Maybe the screen has to be created, so that if the window is fullscreen it will be scaled to fit
        # I then have to create a window with the screen as an argument
