import pyglet

from Core import game, Menu

if __name__ == '__main__':
    game_window = game.GameWindow()

    game_window.main_menu_batch = Menu.Main(game_window)
    game_window.pause_menu_batch = Menu.Pause(game_window)

    pyglet.app.run()
