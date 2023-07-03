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
        for i in self.game.level_manager.active_levels:
            for j in i.gui_list:
                j.interaction(event)

# the main menu class that contains all the elements in the menu and manages them
class Menu:
    def __init__(self, game, level) -> None:
        self.level = level
        self.game = game
        self.elements = []

    # this is used for polymorphism within the menus
    def interaction(self, event):
        pass

    # used to draw the elements in the menu on the screen
    def draw(self, game):
        for i in self.elements:
            i.draw(self.game, self.level)

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
    def __init__(self, game, level, x, y, tags=[]) -> None:
        self.game = game
        self._x = x
        self._y = y
        self.tags = tags
        self.level = level

    # used to draw the element on the screen
    def draw(self, game, level):
        try:
            game.level_manager.loaded_levels[level].screen.blit(self.texture.get_texture(), (self._x, self._y))
        except Exception as e:
            print(e)
            error_messages.polymorphism_rule_violation_made_an_issue(self)

    # used to align the element
    def AlignSelf(self, align, posx, posy, game, level, width, height):
        self.level = level
        posx = game.level_manager.loaded_levels[level].screen.get_width() * posx
        posy = game.level_manager.loaded_levels[level].screen.get_height() * posy
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
    def __init__(self, game, level, texture, posx, posy, align=(AligPos.Left, AligPos.Top), tags=[]) -> None:
        self.texture = game.texture_manager.get_texture(texture)
        posx, posy = self.AlignSelf(align, posx, posy, game, level, self.texture.get_texture().get_width(), self.texture.get_texture().get_height())

        super().__init__(game, level, posx, posy, tags)


# Image element class, inherits from the GUI_element
class GUI_image(GUI_element):
    def __init__(self, game, level, texture, posx, posy, align=(AligPos.Left, AligPos.Top), tags=[]) -> None:
        self.texture = game.texture_manager.get_texture(texture)
        posx, posy = self.AlignSelf(align, posx, posy, game, level, self.texture.get_texture().get_width(), self.texture.get_texture().get_height())

        super().__init__(game, level, posx, posy, tags)


# Text element class, inherits from the GUI_element
class GUI_text(GUI_element):
    def __init__(self, game, level, text, posx, posy, align=(AligPos.Left, AligPos.Top), font="JetBrainsMono-Bold.ttf", size=10, antialias=True, color=(255, 255, 255), tags=[]) -> None:
        self.font = font
        self.size = size
        self.antialias = antialias
        self.color = color
        self.font = pygame.font.Font("textures/fonts/" + font, size)
        self.text = self.font.render(text, antialias, color)
        self.string_text = text
        width = self.text.get_width()
        height = self.text.get_height()
        posx, posy = self.AlignSelf(align, posx, posy, game, level, width, height)
        super().__init__(game, level, posx, posy, tags)

    def update_text(self, text, font="JetBrainsMono-Bold.ttf", size=10, antialias=True, color=(255, 255, 255)):
        self.font = font
        self.size = size
        self.antialias = antialias
        self.color = color
        self.font = pygame.font.Font("textures/fonts/" + font, size)
        self.text = self.font.render(text, antialias, color)
        self.string_text = text

    def draw(self, game, level):
        game.level_manager.loaded_levels[level].screen.blit(self.text, (self._x, self._y))

####################
# MENU DEFINITIONS #
####################

# the menu shown in the beginning of the game
class MainMenu(Menu):
    def __init__(self, game, level) -> None:
        super().__init__(game, level)
        # start button
        self.elements.append(GUI_button(game, level, "gui/button.png", 0.5, 0.4, align=(AligPos.Center, AligPos.Middle), tags=["Start"]))
        # DUNGEON DELVE logo
        self.elements.append(GUI_image(game, level, "gui/logo.png:{Relative_Scale:(0.8;0.8)}", 0.5, 0.2, align=(AligPos.Center, AligPos.Middle), tags=["Logo"]))

    def interaction(self, event):
        # detection if the mouse is pressed and if it is on a button
        if event.type == pygame.MOUSEBUTTONUP:
            for i in self.elements:
                if event.pos[0] > i._x and event.pos[0] < i._x + i.texture.get_texture().get_width() and event.pos[1] > i._y and event.pos[1] < i._y + i.texture.get_texture().get_height():
                    # if its a "Start" button, load the first level
                    if "Start" in i.tags:
                        self.game.level_manager.set_level("level1.json")
                        self.game.level_manager.set_level("fps.json")
                        self.game.level_manager.unset_level("GUI_mainMenu.json")

                        player_object.player(game=self.game, texture="player/default.png:{Relative_Scale:(4;4)}", size_x=64, size_y=64, layer=50)

class FPS(Menu):
    def __init__(self, game, level) -> None:
        super().__init__(game, level)
        self.elements.append(GUI_text(game, level, f"FPS: {self.game.__clock__.get_fps()//1}", 0, 0, align=(AligPos.Left, AligPos.Top)))

    def interaction(self, event):
        for i in self.elements:
            i.update_text(f"FPS: {self.game.__clock__.get_fps()//1}")
