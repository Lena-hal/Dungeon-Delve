import game_class
from pygame.locals import *
import pygame
import error_messages

# the basic Object class, every object inherits from this
class Object:
    def __init__(self, texture="default.png",animated = False, level="level0.lvl", x=0,y=0,size_x=16,size_y=16,layer=0, game = None):
        print(game)
        self.__texture__ = pygame.image.load("textures/" + texture)
        self.animated_texture = animated
        self._level = level
        self._x = x
        self._y = y
        self._xSize = size_x
        self._ySize = size_y
        self.layer = 0
        self.current_game = game
        self.current_frame = 0
        self.max_frame = 8
        self.frame_lenght = 10
        self.render()
        self.unrender()

    def change_texture(self, new_texture="default.png",animated = False, max_frame = 8, frame_lenght = 10):
        self.__texture__ = pygame.image.load("textures/" + new_texture)
        self.animated_texture = animated
        self.max_frame = max_frame
        if (frame_lenght > 0):
            self.frame_lenght = frame_lenght
        else:
            error_messages.animation_short_frame(self)

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

    
    def texture(self):
        if not self.animated_texture:
            return self.__texture__
        else:
            try:
                self.animate()
                frame_width = self.__texture__.get_width()
                frame_height = self.__texture__.get_height()/self.max_frame
                return self.__texture__.subsurface(pygame.Rect(0,frame_height*(self.current_frame//self.frame_lenght),frame_width,frame_height))
            except:
                error_messages.animation_max_frame_exceded(self)
                return self.__texture__
        
    def animate(self):
        if (self.current_frame+1 == self.max_frame*self.frame_lenght):
            self.current_frame = 0
        else:
            self.current_frame+=1




