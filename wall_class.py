import game_object
import texture_class

class Wall(game_object.Object):
    def __init__(self,x,y,width,height,game,level,texture):
        self.layer = 0
        self.texture = game.manager.get_texture(texture,)
        super().__init__(texture, level, x, y, width, height, self.layer, game)
    

