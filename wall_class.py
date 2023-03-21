import game_object

class Wall(game_object.Object):
    def __init__(self,x,y,width,height,game,level):
        self.layer = 0
        texture = self.generate_texture()
        super().__init__(texture, level, x, y, width, height, self.layer, game)
        
    def generate_texture():
        pass
