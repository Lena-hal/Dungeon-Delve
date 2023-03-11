from game_object import *
import game_class
from pygame.locals import *

class player(Object):
    def __init__(self, texture="default.png", level="level0.lvl", x=0, y=0, size_x=16, size_y=16, layer=0):
        super().__init__(texture, level, x, y, size_x, size_y, layer)
    