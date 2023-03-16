from game_object import *
import game_class
from pygame.locals import *

# the trigger object > used for every interaction
class Trigger(Object):
    def __init__(self, texture="trigger_debug.png", level="level0.lvl", x=0, y=0, size_x=16, size_y=16, layer=0, game = None):
        super().__init__(texture, level, x, y, size_x, size_y, layer, game)
        self.current_game.trigger_list.append(self)
    
    def interaction(self, key=None, interaction_author=None):
        if key[K_r]:
            print("R - debug button pressed")