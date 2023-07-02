import game_object

# this class is used to create the walls in the game
class Wall(game_object.Object):
    def __init__(self, wall_data, game, level):

        texture = wall_data["Texture"]
        x = wall_data["X"]
        y = wall_data["Y"]
        width = wall_data["Width"]
        height = wall_data["Height"]
        layer = wall_data["Layer"]
        super().__init__(texture, level, x, y, width, height, layer, game)
        self.texture = self.texture.manager.get_texture(texture)
