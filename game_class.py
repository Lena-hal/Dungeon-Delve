import pygame
import texture_class
import level_class
import renderer
import event_class
import camera_class


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
        self.level_manager = level_class.Level_manager(self)
        self.event_manager = event_class.Event_manager(self)
        self.camera_manager = camera_class.Camera_manager(self)

        # inicialization of the first level
        self.level_manager.set_level("GUI_mainMenu.json")

        # this list contrains every object that listens to any events
        self.trigger_list = []

        # this is the player that is currently in the game
        self.local_player = None

    # the default game loop, it is called every frame to process everything
    def game_loop(self):
        while (True):
            self.event_manager.process_events()
            self.renderer.render()
