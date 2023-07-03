import pygame
import sys
from pygame.locals import QUIT

class Event_manager:
    def __init__(self, game) -> None:
        self.game = game
        self.event_listeners = []

    def add_event_listener(self, listener):
        self.event_listeners.append(listener)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            for i in self.game.level_manager.active_levels:
                for j in i.gui_list:
                    j.interaction(event)

        key_pressed = pygame.key.get_pressed()
        for i in self.event_listeners:
            i.interaction(key=key_pressed, interaction_author=self.game.local_player)
