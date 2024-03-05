import arcade

from pyjam10.config import config
from pyjam10.game import Game


def run():
    game = Game(config())
    game.setup()
    
    arcade.run()
