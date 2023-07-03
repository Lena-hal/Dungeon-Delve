import json
import wall_class
import gui
import game_object

# this manager is used to load levels interact with them
class Level_manager:
    def __init__(self, game) -> None:
        self.game = game
        self.loaded_levels = {}
        self.active_level = None

    # loading a level into memory
    def load_level(self, level_path):
        if level_path not in self.loaded_levels:
            Level(level_path, self.game)

    # setting some level as the active level
    def set_level(self, level_path):
        if level_path not in self.loaded_levels:
            self.load_level(level_path)
        self.active_level = self.loaded_levels[level_path]

# class of any level
class Level:
    def __init__(self, level_path, game) -> None:
        self.game = game
        self.game.level_manager.loaded_levels[level_path] = self
        self.loaded_objects = {}
        self.gui_list = []

        # loading level data
        with open("level_data/" + level_path, "r") as data:
            self.level_data = json.load(data)

        # loading background
        game_object.Object(texture=self.level_data["Data"]["Background"], level=level_path, game=self.game)

        # loading all wall objects
        if "Walls" in self.level_data["Data"]:
            for i in self.level_data["Data"]["Walls"]:
                wall_class.Wall(i, self.game, level_path)

        # loading all GUI objects
        if "Menus" in self.level_data["Data"]:
            loaded_gui_elements = []
            self.loaded_objects[100] = []

            # loading different menus
            for i in self.level_data["Data"]["Menus"]:
                if i == "MainMenu":
                    loaded_gui_elements.append(gui.MainMenu(self.game))

            # adding them to the list of objects and GUI's
            for i in loaded_gui_elements:
                self.loaded_objects[100].append(i)
                self.gui_list.append(i)
