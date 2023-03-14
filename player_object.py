from game_object import *
import game_class
from pygame.locals import *
import math
sqrt2 = math.sqrt(2) # this is for optimalisation (many calculations prevented by precalculating)

class player(Object):
    def __init__(self, texture="default.png", level="level0.lvl", x=0, y=0, size_x=16, size_y=16, layer=0, game = None):
        super().__init__(texture, level, x, y, size_x, size_y, layer, game)
        self.current_game.trigger_list.append(self)
        self.current_game.local_player = self
        self.speed = 5
        
    def interaction(self, key=None, interaction_author=None):
        if interaction_author == self:
            # TODO: fix the bug that if you press 3 keys it lags
            if key[K_w] and not key[K_a] and not key[K_s] and not key[K_d]: # up movement
                self.relative_pos_change(y_change=-self.speed)
            if not key[K_w] and key[K_a] and not key[K_s] and not key[K_d]: # left movement
                self.relative_pos_change(x_change=-self.speed)
            if not key[K_w] and not key[K_a] and not key[K_s] and key[K_d]: # right movement
                self.relative_pos_change(x_change=self.speed)
            if not key[K_w] and not key[K_a] and key[K_s] and not key[K_d]: # down movement
                self.relative_pos_change(y_change=self.speed)
            if key[K_w] and key[K_a] and not key[K_s] and not key[K_d]: # left up
                change = (self.speed/sqrt2)
                self.relative_pos_change(x_change=-change,y_change=-change)
            if not key[K_w] and key[K_a] and key[K_s] and not key[K_d]: # left down
                change = (self.speed/sqrt2)
                self.relative_pos_change(x_change=-change,y_change=change)
            if key[K_w] and not key[K_a] and not key[K_s] and key[K_d]: # right up
                change = (self.speed/sqrt2)
                self.relative_pos_change(x_change=change,y_change=-change)
            if not key[K_w] and not key[K_a] and key[K_s] and key[K_d]: # right down
                change = (self.speed/sqrt2)
                self.relative_pos_change(x_change=change,y_change=change)

    
        
            
    
    