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

    # texture assigment function that tries to use as same textures if possible
    def get_texture(self, texture_path):
        # object can request two types of textures:
        #    original texture - just the path (textures/texture_path.png)
        #    modified texture - the path and after ":" list of modificators in the form {modificator_name: (inputs), ...} (textures/texture_path.png:{modificator_name:inputs,modificator_name:inputs})
        #    user can enter more then 1 argument for 1 modfier so Scale:(1.5,3.4) is valid argument
        mod_string = ""
        mod_dict = {}
        original_path = texture_path
        if ":" in texture_path:
            texture_path, mod_string = texture_path.split(":", 1)
            mod_string = mod_string.replace("{", "").replace("}", "")
            mods = mod_string.split(",")
            for mod in mods:
                mod_name, mod_values = mod.split(":")
                mod_values = mod_values.replace("(", "").replace(")", "").split(";")
                mod_dict[mod_name] = mod_values

            if texture_path in self.texture_data:
                self.texture_data[original_path] = self.texture_data[texture_path].copy()
            else:
                error_messages.texture_manager_invalid_path(texture_path)
        if original_path not in self.texture_data:
            error_messages.texture_manager_invalid_path(original_path)
            original_path = "default/default.png"
            texture_path = "default/default.png"
        if self.texture_data[original_path]["pointer"] is None:
            self.texture_data[original_path]["pointer"] = Texture(texture_path, original_path, mod_dict, self)
        return self.texture_data[original_path]["pointer"]

# the class for all the texture objects, it contains all the texture data and methods to manage it
class Texture:
    def __init__(self, texture, org_path, mod_dict, manager):
        self.manager = manager
        self.path = org_path
        self.file_path = texture
        self.animated_texture = manager.texture_data[self.path]["Animated"]

        if self.animated_texture:
            self.current_frame = 0
            self.max_frame = manager.texture_data[self.path]["Frames"]
            self.frame_lenght = manager.texture_data[self.path]["Default_Frame_Rate"]
        self.__texture__ = pygame.image.load("textures/" + texture)
        if mod_dict != {}:
            self.apply_modificators(mod_dict)

    # returns the canvas object used usually to render the object
    def get_texture(self):
        # animation controller
        if not self.animated_texture:
            return self.__texture__
        else:
            try:
                # this tries to animate the texture, if it fails it returns the original texture
                self.animate()
                frame_width = self.__texture__.get_width()
                frame_height = self.__texture__.get_height() / self.max_frame
                return self.__texture__.subsurface(pygame.Rect(0, frame_height * (self.current_frame // self.frame_lenght), frame_width, frame_height))
            except Exception as e:
                print(e)
                error_messages.animation_max_frame_exceded(self)
                return self.__texture__

    # if texture animated, changes the frame to the next one
    def animate(self):
        if (self.current_frame + 1 == self.max_frame * self.frame_lenght):
            self.current_frame = 0
        else:
            self.current_frame += 1

    # this function is used to apply modificators to the texture
    def apply_modificators(self, mod_dict):
        for mod_name, mod_values in mod_dict.items():
            if mod_name == "Relative_Scale":
                Modificators.Relative_Scale(self, mod_values)
            elif mod_name == "Absolute_Scale":
                Modificators.Absolute_Scale(self, mod_values)
            elif mod_name == "Rotate":
                Modificators.rotate(self, mod_values)
            else:
                error_messages.invalid_texture_modificator(mod_name)

# this class is used to manage all the modificators that can be applied to the texture
class Modificators():
    # scales the texture by relative values eg.: (1.5,3.4)
    def Relative_Scale(texture, mod_values):
        width = texture.__texture__.get_width() * float(mod_values[0])
        height = texture.__texture__.get_height() * float(mod_values[1])
        texture.__texture__ = pygame.transform.scale(texture.__texture__, (width, height))

    # scales the texture by absolute values (pixels) eg.: (20,50)
    def Absolute_Scale(texture, mod_values):
        texture.__texture__ = pygame.transform.scale(texture.__texture__, (float(mod_values[0]), float(mod_values[1])))

    # rotates the texture by the given angle (in degrees) eg.: (90)
    def rotate(texture, mod_values):
        texture.__texture__ = pygame.transform.rotate(texture.__texture__, float(mod_values[0]))
