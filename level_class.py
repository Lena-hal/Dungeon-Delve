import texture_class
import json
import wall_class
class Level:
    def __init__(self,level_path,game) -> None:
        self.game = game
        self.walls = []
        with open(level_path,"r") as data:
            self.level_data = json.load(data)
        self.background = Background(self.level_data["Data"]["Background"],self.game)
        for i in self.level_data["Data"]["Walls"]:
            self.walls.append(wall_class.Wall(i[0],i[1],i[2],i[3],self.game,level_path,i[4]))



class Background:
    def __init__(self,path,game) -> None:
        self.game = game
        self._x = 0
        self._y = 0
        self.texture = game.manager.get_texture(path)
        print(self.texture)
        self.game.render_list.append(self)

