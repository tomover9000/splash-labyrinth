#!/usr/bin/env python3

import pygame
import random
from labyrinth import Labyrinth
#from pygame.locals import *

BLOCK_SIZE = 20
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)


class Game:

    def __init__(self, size):

        self.size = size
        self.screen = pygame.display.set_mode((size * BLOCK_SIZE, size * BLOCK_SIZE))
        pygame.display.set_caption('Splash Labyrinth')
        pygame.time.Clock().tick(60)
        self.Lab = Labyrinth(self.size)
        

    def update(self):
        self.Lab.update()
        pass


    def run(self):
        while True:
            self.draw()
            self.update()

    def draw(self):
        self.screen.fill(BLACK)

        for x in range(self.size) :
            for y in range(self.size) :
                if self.Lab.matrix[x][y] == 1 :
                    pygame.draw.rect(self.screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        
        pygame.display.update()




    
