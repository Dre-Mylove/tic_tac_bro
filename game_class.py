import pygame
from settings import *


class Game:
    def _init_(self):
        pygame.init()
        self.running =True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        while self.running:
            self.get_events()
            self.update()
            self.draw()
        pygame.quit()

    def get_events(self):
        for events in pygame.events.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BF_COLOUR)
        pygame.display.update()