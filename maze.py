#!/usr/bin/env python3

import pygame
import random
#from pygame.locals import *

BLOCK_SIZE = 20
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

width = 40
height = 45

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((width * BLOCK_SIZE, height * BLOCK_SIZE))
        pygame.display.set_caption('Splash Labyrinth')
        pygame.time.Clock().tick(60)
        print("1")
        

    def update(self):
        pass

    def run(self):
        while True:
            self.draw()

    def draw(self):
        self.screen.fill(BLACK)
        pygame.display.update()
        print(2)



def main():
    pygame.display.init()

    game = Game()
    game.run()
    pygame.display.quit()



    
