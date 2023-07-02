import pygame
import error_messages
import enum
import player_object

# this manager has under control everything to do with GUIs - event processing TODO: replace this with a proper event system
class GUI_manager:
    def __init__(self, game) -> None:
        self.game = game

    # this is called for every Menu for every event
    def process_events(self, event):
        for i in self.game.level_manager.active_level.gui_list:
            i.interaction(event)

# the main menu class that contains all the elements in the menu and manages them
class Menu:
    def __init__(self, game) -> None:
        self.game = game
        self.elements = []

    # this is used for polymorphism within the menus
    def interaction(self, event):
        pass

    # used to draw the elements in the menu on the screen
    def draw(self, game):
        for i in self.elements:
            i.draw(self.game)

# enum to represent all the aligment options avalible
class AligPos(enum.Enum):
    Left = 0
    Right = 1
    Center = 2
    Top = 3
    Bottom = 4
    Middle = 5

# class with functions to allign anything to a certain location
class Alignment():
    def Left(x, width):
        return x

    def Right(x, width):
        return x - width

    def Center(x, width):
        return x - (width / 2)

    def Top(y, height):
        return y

    def Bottom(y, height):
        return y - height

    def Middle(y, height):
        return y - (height / 2)

# the basic element class, every element in the GUI must inherit from this
class GUI_element():
    def __init__(self, game, x, y, tags=[]) -> None:
        self.game = game
        self._x = x
        self._y = y
        self.tags = tags

    # used to draw the element on the screen
    def draw(self, game):
        try:
            game.__SURFACE__.blit(self.texture.get_texture(), (self._x, self._y))
        except Exception as e:
            print(e)
            error_messages.polymorphism_rule_violation_made_an_issue(self)

    # used to align the element
    def AlignSelf(self, align, posx, posy, game, width, height):
        posx = game.window_width * posx
        posy = game.window_width * posy
        if align[0] == AligPos.Left:
            posx = Alignment.Left(posx, width)
        if align[0] == AligPos.Right:
            posx = Alignment.Right(posx, width)
        if align[0] == AligPos.Center:
            posx = Alignment.Center(posx, width)

        if align[1] == AligPos.Top:
            posy = Alignment.Top(posy, height)
        if align[1] == AligPos.Bottom:
            posy = Alignment.Bottom(posy, height)
        if align[1] == AligPos.Middle:
            posy = Alignment.Middle(posy, height)
        return posx, posy


# Button element class, inherits from the GUI_element
class GUI_button(GUI_element):
    def __init__(self, game, texture, posx, posy, align=(AligPos.Left, AligPos.Top), tags=[]) -> None:
        self.texture = game.texture_manager.get_texture(texture)
        posx, posy = self.AlignSelf(align, posx, posy, game, self.texture.get_texture().get_width(), self.texture.get_texture().get_height())

        super().__init__(game, posx, posy, tags)


# Image element class, inherits from the GUI_element
class GUI_image(GUI_element):
    def __init__(self, game, texture, posx, posy, align=(AligPos.Left, AligPos.Top), tags=[]) -> None:
        self.texture = game.texture_manager.get_texture(texture)
        posx, posy = self.AlignSelf(align, posx, posy, game, self.texture.get_texture().get_width(), self.texture.get_texture().get_height())

        super().__init__(game, posx, posy, tags)


# Text element class, inherits from the GUI_element
class GUI_text(GUI_element):
    def __init__(self, game, text, posx, posy, align=(AligPos.Left, AligPos.Top), font="JetBrainsMono-Bold.ttf", size=32, antialias=True, color=(0, 0, 0), background=None, tags=[]) -> None:
        posx, posy = self.AlignSelf(align, posx, posy, game)
        self.font = pygame.font.Font("textures/fonts" + font, size)
        self.text = font.render(text, antialias, color, background=None)
        super().__init__(game, posx, posy, tags)

    def draw(self, game):
        game.__SURFACE__.blit(self.text, (self._x, self._y))

####################
# MENU DEFINITIONS #
####################

# the menu shown in the beginning of the game
class MainMenu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        # start button
        self.elements.append(GUI_button(game, "gui/button.png", 0.5, 0.4, align=(AligPos.Center, AligPos.Middle), tags=["Start"]))
        # DUNGEON DELVE logo
        self.elements.append(GUI_image(game, "gui/logo.png:{Relative_Scale:(0.8;0.8)}", 0.5, 0.2, align=(AligPos.Center, AligPos.Middle), tags=["Logo"]))

    def interaction(self, event):
        # detection if the mouse is pressed and if it is on a button
        if event.type == pygame.MOUSEBUTTONUP:
            for i in self.elements:
                if event.pos[0] > i._x and event.pos[0] < i._x + i.texture.get_texture().get_width() and event.pos[1] > i._y and event.pos[1] < i._y + i.texture.get_texture().get_height():
                    # if its a "Start" button, load the first level
                    if "Start" in i.tags:
                        self.game.level_manager.set_level("level1.json")
                        player_object.player(game=self.game, texture="player/default.png:{Relative_Scale:(4;4)}", size_x=64, size_y=64, layer=50)
