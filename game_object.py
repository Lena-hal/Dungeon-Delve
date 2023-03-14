import game_class
from pygame.locals import *
import pygame

# the basic Object class, every object inherits from this
class Object:
    def __init__(self, texture="default.png", level="level0.lvl", x=0,y=0,size_x=16,size_y=16,layer=0, game = None):
        self.__texture__ = pygame.image.load("textures/" + texture)
        self._level = level
        self._x = x
        self._y = y
        self._xSize = size_x
        self._ySize = size_y
        self.layer = 0
        self.current_game = game
        self.render()
        self.unrender()

    def change_texture(self, new_texture="default.png"):
        self.__texture__ = pygame.image.load("textures/" + new_texture)

    def relative_pos_change(self, x_change=0, y_change=0):
        self._x += x_change
        self._y += y_change
    
    def absolute_pos_change(self, new_x=0, new_y=0):
        self._x = new_x
        self._y = new_y

    def change_size(self, new_x_size=16, new_y_size=16):
        self._xSize = new_x_size
        self._ySize = new_y_size
        
    def render(self):
        self.current_game.render_list.append(self)
    
    def unrender(self):
        self.current_game.unrender_list.append(self)



