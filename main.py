import pygame

class game:
    def __init__(self):
        self.fps = 60
        pygame.init()
        self.display = pygame.display.set_mode((1200, 800),0,32)
        pygame.key.set_repeat(1,100)

        
    def fps_render(self,render_list):
        print("a")

hra = game()


