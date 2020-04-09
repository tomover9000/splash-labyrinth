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
        self.Lab = Labyrinth(size)
        

    def input(self):
        event = pygame.event.get()

        if event.type == pygame.KEYDOWN
            if event.key == pygame.K_SPACE
                self.solve()
    

    def solve(self):
        pass

    def update(self):
        self.Lab.update()
        pass


    def run(self):
        while True:
            self.draw()
            self.update()
            self.input()


    def draw(self):
        self.screen.fill(BLACK)

        for x in range(self.Lab.size) :
            for y in range(self.Lab.size) :
                if self.Lab.matrix[x][y] == 1 :
                    pygame.draw.rect(self.screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        
        pygame.display.update()




    
