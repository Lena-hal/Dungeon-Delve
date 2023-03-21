import texture_class
import json
import wall_class
class Level:
    def __init__(self,level_path,game) -> None:
        self.game = game
        with open(level_path,"r") as data:
            self.level_data = json.load(data)
        self.background = Background(self.level_data["Data"]["Background"],self.game)
        for i in self.level_data["Data"]["Walls"]:
            print(i)



class Background:
    def __init__(self,path,game) -> None:
        self.game = game
        self._x = 0
        self._y = 0
        self.texture = texture_class.Texture_manager.get_texture(path)
        print(self.texture)
        self.game.render_list.append(self)

    
Level("level_data/level1.json")