
# the basic Object class, every basic object inherits from this exept for the GUI
class Object:
    def __init__(self, texture="default.png", level="level1.json", x=0, y=0, size_x=16, size_y=16, layer=0, game=None):
        self.texture = game.texture_manager.get_texture(texture)
        if layer not in game.level_manager.loaded_levels[level].loaded_objects:
            game.level_manager.loaded_levels[level].loaded_objects[layer] = []
        game.level_manager.loaded_levels[level].loaded_objects[layer].append(self)
        self.level = game.level_manager.loaded_levels[level]

        self._x = x
        self._y = y
        self._xSize = size_x
        self._ySize = size_y
        self.game = game

    # moves the object with relative coordinates
    def relative_pos_change(self, x_change=0, y_change=0):
        self._x += x_change
        self._y += y_change

    # moves the object with absolute coordinates
    def absolute_pos_change(self, new_x=0, new_y=0):
        self._x = new_x
        self._y = new_y

    # changes the size of the object
    def change_size(self, new_x_size=16, new_y_size=16):
        self._xSize = new_x_size
        self._ySize = new_y_size

    # draws itself on a screen
    def draw(self, game):
        self.level.screen.blit(self.texture.get_texture(), (self._x, self._y))
