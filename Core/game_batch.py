import pyglet

class GameBatch(pyglet.graphics.Batch):
    """ The batch of game graphics, also handles the updates of the positions etc. """

    def __init__(self, *args, **kwargs):
        """ Initializes menu items """
        super(GameBatch, self).__init__(*args, **kwargs)

