import arcade


class Game(arcade.Window):
    def __init__(self, config):
        self.pixel_size = config["window"]["pixel_size"]
        self.player_speed = config["player"]["speed"]

        super().__init__(
            config["window"]["width"]*self.pixel_size,
            config["window"]["height"]*self.pixel_size,
            config["window"]["title"],
            antialiasing=False)

        self.movement_keys = (
            arcade.key.UP,
            arcade.key.DOWN,
            arcade.key.LEFT,
            arcade.key.RIGHT,
        )
        
        self.map = None
        self.scene = None
        self.player = None
        self.camera = None

        self.keys_down = None
        self.footstep = None

    def setup(self):
        self.map = arcade.load_tilemap("maps/01.tmx", self.pixel_size, {
            "Obstacles": {
                "use_spatial_hash": True,
            },
        })
        self.scene = arcade.Scene.from_tilemap(self.map)

        # Extract sprite loaded from map
        self.player = self.scene.get_sprite_list("Player")[0]

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player, self.scene.get_sprite_list("Obstacles"))
        
        self.camera = arcade.Camera(self.width, self.height)

        self.keys_down = set()

        # wind = arcade.load_sound("assets/wind.wav")
        # wind.play(loop=True)
        
        music = arcade.load_sound("assets/music.wav")
        music.play(loop=True)

        self.footstep = arcade.load_sound("assets/footstep.wav")
        self.footstep_player = None

    def center_camera_on_player(self):
        new_x = self.player.center_x - self.camera.viewport_width/2
        new_y = self.player.center_y - self.camera.viewport_height/2

        self.camera.move_to((new_x, new_y))

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key in self.movement_keys:
            if self.footstep_player is None or not self.footstep.is_playing(self.footstep_player):
                self.footstep_player = self.footstep.play(loop=True)

            self.keys_down.add(key)

        self.update_movement()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key in self.movement_keys:
            self.keys_down.remove(key)

            if len(self.keys_down) == 0:
                self.footstep.stop(self.footstep_player)

            if key == arcade.key.UP:
                self.player.change_y = 0

            if key == arcade.key.DOWN:
                self.player.change_y = 0

            if key == arcade.key.RIGHT:
                self.player.change_x = 0

            if key == arcade.key.LEFT:
                self.player.change_x = 0

        self.update_movement()

    def update_movement(self):
        speed = self.player_speed

        if len(self.keys_down) == 2:
            # Roughly root 2 over 2
            speed *= 0.7

        if arcade.key.UP in self.keys_down:
            self.player.change_y = speed

        if arcade.key.DOWN in self.keys_down:
            self.player.change_y = -speed

        if arcade.key.RIGHT in self.keys_down:
            self.player.change_x = speed

        if arcade.key.LEFT in self.keys_down:
            self.player.change_x = -speed

    def on_update(self, delta_time):
        """Movement and game logic"""

        self.physics_engine.update()
        self.center_camera_on_player()

    def on_draw(self):
        self.camera.use()
        self.clear()
        self.scene.draw(filter=arcade.gl.NEAREST)
