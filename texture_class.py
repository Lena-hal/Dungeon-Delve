import pygame
import error_messages
import json
import enum

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
    
    def del_texture(self, pointer):
        keys = [k for k in self.texture_data if self.texture_data[k] == pointer]
        for k in keys:
            del self.texture_data[k]


# this class is used for storing textures
class Texture:
    def __init__(self, texture, manager):
        self.manager = manager
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

class ModifiedTexture(Texture):
    def __init__(self, texture, manager, modifier_list):
        self.modlist = modifier_list
        super().__init__(texture, manager)
        self.users = 1
        self.update_texture_hash()

    def __del__(self):
        self.manager.del_texture(self)

    def get_texture(self):
        self.users+=1
        return super().get_texture()
    
    def take_out_trash(self):
        if self.users == 0:
            self.__del__()
        else:
            self.users = 0
    def update_texture_hash(self):
        self.hash = hash(self.__texture__)



class Modificate:
    def scale_by_pixel(texture,new_size):
        
        texture.__texture__ = pygame.transform.scale(texture.__texture__, new_size)
    
    def scale_by_ratio(texture,ratio):
        width = texture.get_width()*ratio
        height = texture.get_height()*ratio
        texture.__texture__ = pygame.transform.scale(texture.__texture__,(width,height))

