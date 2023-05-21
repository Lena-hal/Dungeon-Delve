import json
import wall_class
import gui
class Level:
    def __init__(self,level_path,game) -> None:
        self.game = game
        self.walls = []
        game.gui_manager.active_menus = []
        with open(level_path,"r") as data:
            self.level_data = json.load(data)
        self.background = Background(self.level_data["Data"]["Background"],self.game)
        if "Walls" in self.level_data["Data"]:
            for i in self.level_data["Data"]["Walls"]:
                self.walls.append(wall_class.Wall(i,self.game,level_path))

        if "Menus" in self.level_data["Data"]:
            for i in self.level_data["Data"]["Menus"]:
                if i == "MainMenu":
                    self.game.gui_manager.active_menus.append(gui.MainMenu(self.game))
            




class Background:
    def __init__(self,path,game) -> None:
        self.game = game
        self._x = 0
        self._y = 0
        self.texture = game.manager.get_texture(path)
        print(self.texture)
        self.game.render_list.append(self)
    def draw(self,game):
        self.game.__SURFACE__.blit(self.texture.get_texture(),(self._x,self._y))
    

