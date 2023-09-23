import arcade

from pyjam7.config import config
from pyjam7.game import Game


def run():
    game = Game(config())
    game.setup()
    
    arcade.run()
