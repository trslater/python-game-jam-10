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
        
        self.map = None
        self.scene = None
        self.player = None
        self.camera = None

    def setup(self):
        self.map = arcade.load_tilemap("maps/01.tmx", self.pixel_size, {
            "Walls": {
                "use_spatial_hash": True,
            },
        })
        self.scene = arcade.Scene.from_tilemap(self.map)

        # Extract sprite loaded from map
        self.player = self.scene.get_sprite_list("Player")[0]

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player, self.scene.get_sprite_list("Obstacles"))
        
        self.camera = arcade.Camera(self.width, self.height)

    def center_camera_on_player(self):
        new_x = self.player.center_x - self.camera.viewport_width/2
        new_y = self.player.center_y - self.camera.viewport_height/2

        self.camera.move_to((new_x, new_y))

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.change_y = self.player_speed
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.change_y = -self.player_speed
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = -self.player_speed
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = self.player_speed
    
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 0
    
    def on_update(self, delta_time):
        """Movement and game logic"""

        self.physics_engine.update()
        self.center_camera_on_player()

    def on_draw(self):
        self.camera.use()
        self.clear()
        self.scene.draw(filter=arcade.gl.NEAREST)
