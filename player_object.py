from game_object import *
from pygame.locals import *
import math
sqrt2 = math.sqrt(2) # this is for optimalisation (many calculations prevented by precalculating)

class player(Object):
    def __init__(self, texture="default.png", level="level1.json", x=0, y=0, size_x=16, size_y=16, layer=0, game = None):
        super().__init__(texture, level, x, y, size_x, size_y, layer, game)
        self.current_game.trigger_list.append(self)
        self.current_game.local_player = self
        self.speed = 5
        
    def interaction(self, key=None, interaction_author=None):
        if interaction_author == self:
            mapping = {
    # W     A      S    D
    (True, True, True, True): None,
    (True, True, True, False): lambda: self.relative_pos_change(x_change=-self.speed), #left
    (True, True, False, True): lambda: self.relative_pos_change(y_change=-self.speed), # up
    (True, True, False, False): lambda: self.relative_pos_change(x_change=-(self.speed/sqrt2),y_change=-(self.speed/sqrt2)), # left up
    (True, False, True, True): lambda: self.relative_pos_change(x_change=self.speed), # right
    (True, False, True, False): None, 
    (True, False, False, True): lambda: self.relative_pos_change(x_change=(self.speed/sqrt2),y_change=-(self.speed/sqrt2)), # right up
    (True, False, False, False): lambda: self.relative_pos_change(y_change=-self.speed), # up
    (False, True, True, True): lambda: self.relative_pos_change(y_change=self.speed), # down
    (False, True, True, False): lambda: self.relative_pos_change(x_change=-(self.speed/sqrt2),y_change=(self.speed/sqrt2)), # left down
    (False, True, False, True): None,
    (False, True, False, False): lambda: self.relative_pos_change(x_change=-self.speed), # left
    (False, False, True, True): lambda: self.relative_pos_change(x_change=(self.speed/sqrt2),y_change=(self.speed/sqrt2)), # right down
    (False, False, True, False): lambda: self.relative_pos_change(y_change=self.speed), # down
    (False, False, False, True): lambda: self.relative_pos_change(x_change=self.speed), # right
    (False, False, False, False): None,
                    }
            func = mapping.get((key[K_w], key[K_a], key[K_s], key[K_d]), lambda: None)
            if func is not None:
                func()
    
        
            
    
    