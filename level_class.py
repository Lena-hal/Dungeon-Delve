import json
import wall_class
import gui
import game_object
import pygame

# this manager is used to load levels interact with them
class Level_manager:
    def __init__(self, game) -> None:
        self.game = game
        self.loaded_levels = {}
        self.active_levels = []

    # loading a level into memory
    def load_level(self, level_path):
        if level_path not in self.loaded_levels:
            Level(level_path, self.game)

    # setting some level as the active level
    def set_level(self, level_path):
        if level_path not in self.loaded_levels:
            self.load_level(level_path)
        self.active_levels.append(self.loaded_levels[level_path])

    def unset_level(self, level_path):
        if level_path in self.loaded_levels:
            self.active_levels.remove(self.loaded_levels[level_path])

# class of any level
class Level():
    def __init__(self, level_path, game) -> None:
        self.game = game
        self.game.level_manager.loaded_levels[level_path] = self
        self.loaded_objects = {}
        self.gui_list = []

        # loading level data
        with open("level_data/" + level_path, "r") as data:
            self.level_data = json.load(data)

        # loading the level dimensions
        self.movable = self.level_data["Data"]["Movable"]
        self._x = self.level_data["Data"]["PosX"] * self.game.window_width
        self._y = self.level_data["Data"]["PosY"] * self.game.window_width
        self.width = self.level_data["Data"]["SizeX"] * self.game.window_width
        self.height = self.level_data["Data"]["SizeY"] * self.game.window_height

        self.screen = pygame.Surface((self.width, self.height)).convert_alpha()

        # loading background
        if "Background" in self.level_data["Data"]:
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
                    loaded_gui_elements.append(gui.MainMenu(self.game, level_path))
                if i == "FPS":
                    loaded_gui_elements.append(gui.FPS(self.game, level_path))
                if i == "Debug":
                    loaded_gui_elements.append(gui.Debug(self.game, level_path))

            # adding them to the list of objects and GUI's
            for i in loaded_gui_elements:
                self.loaded_objects[100].append(i)
                self.gui_list.append(i)
