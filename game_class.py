import pygame
import sys
import texture_class
import level_class
import gui
import renderer
from pygame.locals import QUIT


class game:
    """
    this is the main class that controls everything happening in the game
    """
    def __init__(self, FPS=60, X=1280, Y=960, description="Dungeon Delve"):
        self.window_width = X
        self.window_height = Y
        self.FPS = FPS

        # inicialization of all pygame modules
        pygame.init()
        pygame.display.set_caption(description)
        pygame.key.set_repeat(1, 100)
        self.__SURFACE__ = pygame.display.set_mode(size=(self.window_width, self.window_height), flags=0, depth=64)
        self.__clock__ = pygame.time.Clock()

        # manager inicializers
        self.texture_manager = texture_class.Texture_manager()
        self.renderer = renderer.Render_manager(self)
        self.gui_manager = gui.GUI_manager(self)
        self.level_manager = level_class.Level_manager(self)

        # inicialization of the first level
        self.level_manager.set_level("GUI_mainMenu.json")

        # this list contrains every object that listens to any events
        self.trigger_list = []

        # this is the player that is currently in the game
        self.local_player = None

    # used to render the game frame and update the fps
    def fps_render(self):
        self.renderer.render()
        self.delta_time = self.__clock__.tick(self.FPS)

        pygame.display.update()
        # pygame.display.flip()

    # used to process all the events that happen in the game TODO: create event manager to manage this
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            self.gui_manager.process_events(event)

        key_pressed = pygame.key.get_pressed()
        for i in self.trigger_list:
            i.interaction(key=key_pressed, interaction_author=self.local_player)

    # the default game loop, it is called every frame to process everything
    def game_loop(self):
        while (True):
            # TODO: add a better way of showing fps count
            # print(self.__clock__.get_fps())
            self.event_loop()
            self.fps_render()
