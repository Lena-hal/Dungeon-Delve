import pygame
import sys
from pygame.locals import QUIT

class Event_manager:
    def __init__(self, game) -> None:
        self.game = game
        self.event_listeners = []
        self.tick_listeners = []

    def add_event_listener(self, listener):
        self.event_listeners.append(listener)

    def add_tick_listener(self, listener):
        self.tick_listeners.append(listener)

    def process_events(self):
        for i in self.tick_listeners:
            i.tick()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            for i in self.game.level_manager.active_levels:
                for j in i.gui_list:
                    j.interaction(event)

        key_pressed = pygame.key.get_pressed()

        # activation of the debug mode
        if key_pressed[pygame.K_F3]:
            self.game.debug_mode = not self.game.debug_mode
            if self.game.debug_mode:
                self.game.level_manager.unset_level("fps.json")
                self.game.level_manager.set_level("debug.json")
            else:
                self.game.level_manager.set_level("fps.json")
                self.game.level_manager.unset_level("debug.json")

        for i in self.event_listeners:
            i.interaction(key=key_pressed, interaction_author=self.game.local_player)
