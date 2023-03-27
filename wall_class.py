import game_object
import texture_class

class Wall(game_object.Object):
    def __init__(self,wall_data,game,level,texture):

        self.texture = game.manager.get_texture(texture)
        x = wall_data["X"]
        y = wall_data["Y"]
        width = wall_data["Width"]
        height = wall_data["Height"]
        scale = wall_data["Scale"]
        layer = wall_data["Layer"]
        super().__init__(texture, level, x, y, width, height, layer, game)
    

