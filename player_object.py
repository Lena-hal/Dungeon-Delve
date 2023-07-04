import game_object
from pygame.locals import K_w, K_a, K_s, K_d
import math
sqrt2 = math.sqrt(2)  # this is for optimalisation (many calculations prevented by precalculating)

# this class is a player object, it inherits from game_object.Object
class player(game_object.Object):
    def __init__(self, texture="default.png", level="level1.json", x=0, y=0, size_x=16, size_y=16, layer=0, game=None):
        super().__init__(texture, level, x, y, size_x, size_y, layer, game)
        self.game.trigger_list.append(self)
        self.game.local_player = self
        self.speed = 300  # movement speed
        self.game.event_manager.add_event_listener(self)

    # this function is called when something interacts with the player
    def interaction(self, key=None, interaction_author=None):
        if interaction_author == self:
            # truth table for movement
            mapping = {
                #  W     A      S    D
                (True, True, True, True): None,
                (True, True, True, False): lambda: self.game.camera_manager.move(x_change=-self.speed),  # left
                (True, True, False, True): lambda: self.game.camera_manager.move(y_change=-self.speed),  # up
                (True, True, False, False): lambda: self.game.camera_manager.move(x_change=-(self.speed / sqrt2), y_change=-(self.speed / sqrt2)),  # left up
                (True, False, True, True): lambda: self.game.camera_manager.move(x_change=self.speed),  # right
                (True, False, True, False): None,
                (True, False, False, True): lambda: self.game.camera_manager.move(x_change=(self.speed / sqrt2), y_change=-(self.speed / sqrt2)),  # right up
                (True, False, False, False): lambda: self.game.camera_manager.move(y_change=-self.speed),  # up
                (False, True, True, True): lambda: self.game.camera_manager.move(y_change=self.speed),  # down
                (False, True, True, False): lambda: self.game.camera_manager.move(x_change=-(self.speed / sqrt2), y_change=(self.speed / sqrt2)),  # left down
                (False, True, False, True): None,
                (False, True, False, False): lambda: self.game.camera_manager.move(x_change=-self.speed),  # left
                (False, False, True, True): lambda: self.game.camera_manager.move(x_change=(self.speed / sqrt2), y_change=(self.speed / sqrt2)),  # right down
                (False, False, True, False): lambda: self.game.camera_manager.move(y_change=self.speed),  # down
                (False, False, False, True): lambda: self.game.camera_manager.move(x_change=self.speed),  # right
                (False, False, False, False): None,
            }
            func = mapping.get((key[K_w], key[K_a], key[K_s], key[K_d]), lambda: None)
            if func is not None:
                func()
