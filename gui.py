import pygame
import gameStatusEnum
import error_messages
import enum
import level_class

class GUI_manager:
    def __init__(self,game) -> None:
        self.game = game
        self.active_menus = []
        self.menus = []
        
    
    def process_events(self,event):
        for i in self.active_menus:
            i.interaction(event)
    
    def render(self):
        for i in self.active_menus:
            i.render()

        


class Menu:
    def __init__(self,game) -> None:
        self.game = game
        self.manager = game.gui_manager
        self.game.gui_list.append(self)
        self.elements = []
    
    def interaction(self,event):
        pass

    def render(self):
        for i in self.elements:
            i.draw(self.game)
    

class AligPos(enum.Enum):
    Left = 0
    Right = 1
    Center = 2
    Top = 3
    Bottom = 4
    Middle = 5

class MainMenu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.BUTTON_WIDTH = 200
        self.BUTTON_HEIGHT = 100
        self.BUTTON_SPACING = 100
        self.elements.append(GUI_button(game, "gui/button.png",0.5,0.4,align=(AligPos.Center, AligPos.Middle),tags=["Start"]))
        self.elements.append(GUI_image(game, "gui/logo.png:{Relative_Scale:(0.8;0.8)}",0.5,0.2,align=(AligPos.Center, AligPos.Middle),tags=["Logo"]))
        

    def interaction(self,event):
        if event.type == pygame.MOUSEBUTTONUP:
            for i in self.elements:
                if event.pos[0] > i._x and event.pos[0] < i._x + i.texture.get_texture().get_width() and event.pos[1] > i._y and event.pos[1] < i._y + i.texture.get_texture().get_height():
                    if "Start" in i.tags:
                        self.game.game_status  = gameStatusEnum.gameStatus.ONLINE
                        self.game.reload_background()
                        self.game.level = level_class.Level("level_data/level1.json", self.game)

class GUI_element():
    def __init__(self, game, x, y, tags=[]) -> None:
        self.game = game
        self._x = x
        self._y = y
        self.game.gui_render_list.append(self)
        self.tags = tags
    
    def draw(self, game):
        try:
            game.__SURFACE__.blit(self.texture, (self._x, self._y))
            error_messages.polymorphism_rule_violation(self)
        except:
            error_messages.polymorphism_rule_violation_made_an_issue(self)

    def AlignSelf(self,align, posx, posy, game, width, height):
        posx = game.window_width*posx
        posy = game.window_width*posy
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

class GUI_button(GUI_element):
    def __init__(self, game, texture, posx, posy, align=(AligPos.Left, AligPos.Top), tags=[]) -> None:
        self.texture = game.manager.get_texture(texture)
        posx, posy = self.AlignSelf(align, posx, posy, game, self.texture.get_texture().get_width(), self.texture.get_texture().get_height())
        
        super().__init__(game, posx, posy,tags)
    
    def draw(self, game):
        game.__SURFACE__.blit(self.texture.get_texture(), (self._x, self._y))
    

class GUI_image(GUI_element):
    def __init__(self, game, texture, posx, posy, align=(AligPos.Left, AligPos.Top), tags=[]) -> None:
        self.texture = game.manager.get_texture(texture)
        posx, posy = self.AlignSelf(align, posx, posy, game, self.texture.get_texture().get_width(), self.texture.get_texture().get_height())
        
        super().__init__(game, posx, posy,tags)

    def draw(self, game):
        game.__SURFACE__.blit(self.texture.get_texture(), (self._x, self._y))
    
        
class GUI_text(GUI_element):
    def __init__(self, game,text, posx, posy, align=(AligPos.Left, AligPos.Top), font="JetBrainsMono-Bold.ttf", size=32, antialias=True, color=(0,0,0),background=None, tags=[]) -> None:
        posx, posy = self.AlignSelf(align, posx, posy, game)
        self.font = pygame.font.Font("textures/fonts"+font,size)
        self.text = font.render(text,antialias,color,background=None)
        super().__init__(game, posx, posy, tags)
    
    def draw(self, game):
        game.__SURFACE__.blit(self.text, (self._x, self._y))
    


class Alignment():
    def Left(x, width):
        return x
    
    def Right(x, width):
        return x-width
    
    def Center(x, width):
        return x-(width/2)
    
    def Top(y, height):
        return y
    
    def Bottom(y, height):
        return y-height
    
    def Middle(y, height):
        return y-(height/2)

