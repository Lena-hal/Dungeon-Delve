import pygame
import threading
from enum import Enum
from pygame.locals import *
import sys

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
        self.FPS = FPS
        pygame.init()
        
        self.__texture__ = pygame.image.load("textures/backgrounds/default.png") # background texture of current level 
        # TODO: find a better way of implementing background, because this is bad
        self.trigger_list = []
        self.render_list = []
        self.unrender_list = []

        self.__SURFACE__ = pygame.display.set_mode(size=(X, Y),flags=0,depth=64)
        self.__SURFACE__.blit(self.__texture__, (0,0))
        pygame.display.set_caption(description)

        self.__clock__ = pygame.time.Clock()
        self.game_status = gameStatus.ONLINE
        self.local_player = None
        

        pygame.key.set_repeat(1,100)
    
    def fps_render(self):
        for i in self.unrender_list:
            # TODO: if optimalization needed add: dynamically change the size of unrendering for each enitity because _xSize*3 is sometimes too big 
            self.__SURFACE__.blit(self.__texture__, ((i._x-i._xSize),(i._y-i._ySize)), area=((i._x-i._xSize),(i._y-i._ySize),i._xSize*3,i._ySize*3))

        for i in self.render_list:
            # TODO add the layer mechanic
            self.__SURFACE__.blit(i.texture(), (i._x,i._y))

        pygame.display.update()
        self.__clock__.tick(self.FPS)
    
    def event_loop(self):
        for event in pygame.event.get(): #ovládání eventů
            if event.type == QUIT: # vypínání hry
                pygame.quit()
                sys.exit()
        
        key_pressed = pygame.key.get_pressed()
        for i in self.trigger_list:
            i.interaction(key=key_pressed,interaction_author=self.local_player)

    
    def game_loop(self):
        while (self.game_status == gameStatus.ONLINE):
            self.event_loop()
            self.fps_render()
    
    


    
