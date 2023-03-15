import pygame
import error_messages

# this class is used for all things with it's own texture (player, trigger...)
class Texture:
    def __init__(self, texture, animated, ):
        self.current_frame = 0
        self.max_frame = 8
        self.frame_lenght = 10
        self.__texture__ = pygame.image.load("textures/" + texture)
        self.animated_texture = animated
    
    # returns the canvas object used usually to render the object
    def get_texture(self):
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
    
    # if texture animated, changes the frame to the next one
    def animate(self):
        if (self.current_frame+1 == self.max_frame*self.frame_lenght):
            self.current_frame = 0
        else:
            self.current_frame+=1

    # used to change the texture 
    def change_texture(self, new_texture="default.png",animated = False, max_frame = None, frame_lenght = 10):
        self.__texture__ = pygame.image.load("textures/" + new_texture)
        self.animated_texture = animated

        # if the lenght of animation is not set, it tries to find the lenght based on the height of the texture
        if (max_frame == None):
            self.max_frame = self.get_animation_lenght()
        elif (max_frame > 0):
            self.max_frame = max_frame
        else:
            error_messages.animation_too_small_max_frame(self)

        if (frame_lenght > 0):
            self.frame_lenght = frame_lenght
        else:
            error_messages.animation_short_frame(self)

    # returns the lenght of the animation based on the height of the texture
    def get_animation_lenght(self):
        texture_width= self.__texture__.get_width()
        texture_height = self.__texture__.get_height()
        return texture_height//texture_width