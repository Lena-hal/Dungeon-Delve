import pygame
import error_messages
import json

# this class is used to manage all the texture requests, preventing extra texture loading
class Texture_manager:
    __instance = None

    def __init__(self):
        with open("textures/texture_index.json", "r") as index:
            self.texture_data = json.load(index)
            for i, j in self.texture_data.items():
                j["pointer"] = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def get_texture(self, texture_path):
        if texture_path in self.texture_data:
            if self.texture_data[texture_path]["pointer"] == None:
                self.texture_data[texture_path]["pointer"] = Texture(texture_path,self)
                return self.texture_data[texture_path]["pointer"]
            else:
                return self.texture_data[texture_path]["pointer"]
        else:
            error_messages.texture_manager_invalid_path(texture_path)

# this class is used for storing textures
class Texture:
    def __init__(self, texture, manager):
        self.path = texture
        self.animated_texture = manager.texture_data[self.path]["Animated"]
        if self.animated_texture:
            self.current_frame = 0
            self.max_frame = manager.texture_data[self.path]["Frames"]
            self.frame_lenght = manager.texture_data[self.path]["Default_Frame_Rate"]
            
        self.__texture__ = pygame.image.load("textures/" + texture)
        
    
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


