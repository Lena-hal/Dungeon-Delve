import pygame
import threading
from enum import Enum
from pygame.locals import *
import sys
import texture_class
import pygame_gui

class gameStatus(Enum):
    # this status sets how the game should act
    ONLINE = 1
    OFFLINE = 2
    PAUSED = 3
    IDLE = 4
    ERROR = 5


class game:
    # inicialization of the game, all the local stuff is set here
    def __init__(self, FPS=60, X=1280,Y=960,description="Test Game Window, see docs and more at: https://github.com/Lena-hal"):
        self.window_width = X
        self.window_height = Y
        self.FPS = FPS
        pygame.init()
        self.gui_manager = pygame_gui.UIManager((self.window_width, self.window_height), "textures/gui_theme.json")
        self.manager = texture_class.Texture_manager()

        self.__texture__ = self.manager.get_texture("default/default_bg.png") # background texture of current level 
        # TODO: find a better way of implementing background, because this is bad
        self.trigger_list = []
        self.render_list = []
        self.unrender_list = []
        self.gui_list = []
        self.gui_render_list = []

        self.__SURFACE__ = pygame.display.set_mode(size=(self.window_width, self.window_height),flags=0,depth=64)
        self.reload_background()
        pygame.display.set_caption(description)

        self.__clock__ = pygame.time.Clock()
        self.game_status = gameStatus.PAUSED
        self.local_player = None
        

        pygame.key.set_repeat(1,100)
    
    def reload_background(self):
        self.__SURFACE__.blit(self.__texture__.get_texture(), (0,0))

    def fps_render(self):
        if self.game_status == gameStatus.ONLINE:
            for i in self.unrender_list:
                # TODO: if optimalization needed add: dynamically change the size of unrendering for each enitity because _xSize*3 is sometimes too big 
                self.__SURFACE__.blit(self.__texture__.get_texture(), ((i._x-i._xSize),(i._y-i._ySize)), area=((i._x-i._xSize),(i._y-i._ySize),i._xSize*3,i._ySize*3))

            for i in self.render_list:
                # TODO add the layer mechanic
                self.__SURFACE__.blit(i.texture.get_texture(), (i._x,i._y))

        self.time_delta = self.__clock__.tick(self.FPS)/1000

        if self.game_status == gameStatus.PAUSED:
            self.gui_manager.update(self.time_delta)
            self.gui_manager.draw_ui(self.__SURFACE__)

            for i in self.gui_render_list:
                self.__SURFACE__.blit(i.texture.get_texture(), (i._x,i._y))

        pygame.display.update()


    
    def event_loop(self):
        for event in pygame.event.get(): #ovládání eventů
            if event.type == QUIT: # vypínání hry
                pygame.quit()
                sys.exit()
            self.gui_manager.process_events(event)
            for i in self.gui_list:
                i.interaction(event)
        
        key_pressed = pygame.key.get_pressed()
        for i in self.trigger_list:
            i.interaction(key=key_pressed,interaction_author=self.local_player)

    
    def game_loop(self):
        while (True):
            self.event_loop()
            self.fps_render()
    
    


    
