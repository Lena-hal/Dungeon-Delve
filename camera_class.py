import enum

class Camera_mode(enum.Enum):
    static = 1,
    level = 2,
    dynamic = 3

class Camera_manager:
    def __init__(self, game) -> None:
        self.mode = Camera_mode.static
        self.game = game
        self.zoom = 1
        self._x = 0
        self._y = 0

    def move(self, x_change=0, y_change=0):
        if self.mode == Camera_mode.static or self.mode == Camera_mode.level:
            self.game.local_player.relative_pos_change(x_change * self.game.delta_time, y_change * self.game.delta_time)
        else:
            for i in self.game.level_manager.active_levels:
                if i.movable:
                    for j in i.loaded_objects:
                        if j != 50:  # preventing the player moving with other object
                            for k in i.loaded_objects[j]:
                                k.relative_pos_change(x_change * self.game.delta_time, y_change * self.game.delta_time)
