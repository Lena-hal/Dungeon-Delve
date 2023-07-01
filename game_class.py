import pygame
from pygame.locals import *
import sys
import texture_class
import pygame_gui
import level_class
import gui
import gameStatusEnum
import renderer




class game:
    # inicialization of the game, all the local stuff is set here
    def __init__(self, FPS=60, X=1280,Y=960,description="Dungeon Delve"):
        self.window_width = X
        self.window_height = Y
        self.FPS = FPS
        pygame.init()
        # manager inicializers
        self.texture_manager = texture_class.Texture_manager()
        self.renderer = renderer.Render_manager(self)
        self.gui_manager = gui.GUI_manager(self)
        self.level_manager = level_class.Level_manager(self)

        self.level_manager.set_level("GUI_mainMenu.json")

        self.trigger_list = []
        self.__SURFACE__ = pygame.display.set_mode(size=(self.window_width, self.window_height),flags=0,depth=64)
        self.reload_background()
        pygame.display.set_caption(description)

        self.__clock__ = pygame.time.Clock()
        self.game_status = gameStatusEnum.gameStatus.PAUSED
        self.local_player = None
        

        pygame.key.set_repeat(1,100)
    
    def reload_background(self):
        self.__SURFACE__.blit(self.level_manager.active_level.background.texture.get_texture(), (0,0))

    def fps_render(self):
        self.renderer.render()
        self.__clock__.tick(self.FPS)


        pygame.display.update()


    
    def event_loop(self):
        for event in pygame.event.get(): #ovládání eventů
            if event.type == QUIT: # vypínání hry
                pygame.quit()
                sys.exit()
            self.gui_manager.process_events(event)
        
        key_pressed = pygame.key.get_pressed()
        for i in self.trigger_list:
            i.interaction(key=key_pressed,interaction_author=self.local_player)

    
    def game_loop(self):
        while (True):
            # TODO: add a better way of showing fps count print(self.__clock__.get_fps())
            # print(self.__clock__.get_fps())
            self.event_loop()
            self.fps_render()
    
    


    
