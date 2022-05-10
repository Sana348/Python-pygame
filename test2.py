
from pygame.locals import *
import pygame

class Game:
    def __init__(self):
        self._running = True

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((640,480), pygame.HWSURFACE)
        pygame.display.set_caption('Pygame example')

        self._running = True
       
    def on_render(self):
        self._display_surf.fill((0,0,0))
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
           
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            
            self.on_render()
self.on_cleanup()
 
if __name__ == "__main__" :
    game = Game()
    game.on_execute()
