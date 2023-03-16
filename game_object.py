import game_class
from pygame.locals import *
import pygame
import error_messages
import texture_class

# the basic Object class, every object inherits from this
class Object:
    def __init__(self, texture="default.png", level="level0.lvl", x=0,y=0,size_x=16,size_y=16,layer=0, game = None):
        self.texture = game.manager.get_texture(texture)
        self._level = level
        self._x = x
        self._y = y
        self._xSize = size_x
        self._ySize = size_y
        self.layer = 0
        self.current_game = game
        self.render()
        self.unrender()


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
        
    # adds the object to the list of entities to render
    def render(self):
        self.current_game.render_list.append(self)
    
    # removes the object from the list of renderable entities
    def stop_rendering(self):
        if self in self.current_game.render_list:
            self.current_game.render_list.pop(self)
            
    
    # adds the object to the list of entities that shloud be rerendered every frame
    def unrender(self):
        self.current_game.unrender_list.append(self)
    
    # removes the object to the list of entities that shloud be rerendered every frame
    def stop_unrendering(self):
        if self in self.current_game.unrender_list:
            self.current_game.unrender_list.pop(self)

    # removes all the dependencies to itself in the code (kills itself)
    def remove(self):
        self.stop_rendering()
        self.stop_unrendering()



    
    
        
    




