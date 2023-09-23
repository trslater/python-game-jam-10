import arcade


class Game(arcade.Window):
    def __init__(self, config):
        super().__init__(config["window"]["width"], config["window"]["height"],
                         config["window"]["title"])

    def on_draw(self):
        self.clear()
