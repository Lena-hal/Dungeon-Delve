import pygame
import threading
from enum import Enum
from pygame.locals import *
import sys

class gameStatus(Enum):
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

        self.trigger_list = []
        self.render_list = []

        self.__SURFACE__ = pygame.display.set_mode(size=(X, Y),flags=0,depth=64)
        pygame.display.set_caption(description)

        self.__clock__ = pygame.time.Clock()
        self.game_status = gameStatus.ONLINE

        pygame.key.set_repeat(1,100)
    
    def fps_render(self):
        pygame.display.update()
        self.__clock__.tick(self.FPS)
    
    def event_loop(self):
        for event in pygame.event.get(): #ovládání eventů
            if event.type == QUIT: # vypínání hry
                pygame.quit()
                sys.exit()
        
        key_pressed = pygame.key.get_pressed()
        for i in self.trigger_list:
            i.interaction(key=key_pressed)

    
    def game_loop(self):
        while (self.game_status == gameStatus.ONLINE):
            self.event_loop()
            self.fps_render()
    


    
