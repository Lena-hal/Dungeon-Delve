import game_class
from pygame.locals import *

# the basic Object class, every object inherits from this
class Object:
    def __init__(self, texture="default.png", level="level0.lvl", x=0,y=0,size_x=16,size_y=16,layer=0):
        self.__texture__ = texture
        self._level = level
        self._x = x
        self._y = y
        self._xSize = size_x
        self._ySize = size_y
        self.layer = 0

    def render(self):
        game_class.game.render_list.append((self.__texture__,0))
    
    def unrender(self):
        pass
        # TODO add the self erase function



