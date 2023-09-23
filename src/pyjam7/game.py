import arcade


class Game(arcade.Window):
    def __init__(self):
        super().__init__(320, 200)

    def on_draw(self):
        self.clear()
