import pygame
import pygame_gui
from game_class import gameStatus


class Menu:
    def __init__(self,game) -> None:
        self.game = game
        self.manager = game.gui_manager
        self.game.gui_list.append(self)
        
class MainMenu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.BUTTON_WIDTH = 200
        self.BUTTON_HEIGHT = 100
        self.BUTTON_SPACING = 100
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.game.window_width/2-(0.5*self.BUTTON_WIDTH), self.game.window_height/2-(0.5*self.BUTTON_HEIGHT)+self.BUTTON_SPACING), (self.BUTTON_WIDTH, self.BUTTON_HEIGHT)),text='Enter the Dungeon', manager=self.manager)
        self.logo = GUI_image(game, "gui/logo.png", game.window_width/2, game.window_height/2)
        

    def interaction(self,event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.hello_button:
                self.game.game_status  = gameStatus.ONLINE
                self.game.reload_background()

class GUI_element():
    def __init__(self, game, x, y) -> None:
        self.game = game
        self._x = x
        self._y = y
        self.game.gui_render_list.append(self)

class GUI_image(GUI_element):
    def __init__(self, game, texture, x, y) -> None:
        super().__init__(game, x, y)
        self.texture = self.game.manager.get_texture(texture)
        self.game.gui_render_list.append(self)
