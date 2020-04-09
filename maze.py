#!/usr/bin/env python3

import pygame
import random
from labyrinth import Labyrinth
from pygame.locals import *

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
        events = pygame.event.get()

        for event in events :
            if event.type == KEYDOWN :
                if event.key == K_SPACE :
                    self.solve(0, 1)
            if event.type == KEYUP :
                if event.key == K_SPACE :
                    self.Lab.stopDestroyWalls()
            if event.type == QUIT :
                self.state = "quit"

    def solve(self, x, y) :
        # marcam caile trecute cu 2
        self.draw()
        
        self.Lab.printLabyrinth()
        if x == self.Lab.size - 1 and y == self.Lab.size - 2 :
            self.Lab.matrix[x][y] = 2
            return True 

        if self.Lab.matrix[x][y] != 0 and self.Lab.matrix[x][y] != 2  and self.Lab.matrix[x][y] != 3:

            self.Lab.matrix[x][y] = 2
            
            # jos
            if self.solve(x + 1, y) :
                return True 
            # dreapta
            if self.solve(x, y + 1) :
                return True 
            # stanga
            if self.solve(x, y - 1) :
                return True 
            # sus
            if self.solve(x - 1, y) :
                return True 
            
            self.Lab.matrix[x][y] = 3
            return False

        return False

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
                    pygame.draw.rect(self.screen, WHITE, (y * BLOCK_SIZE, x * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                if self.Lab.matrix[x][y] == 2 :
                    pygame.draw.rect(self.screen, RED, (y * BLOCK_SIZE, x * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                if self.Lab.matrix[x][y] == 3 :
                    pygame.draw.rect(self.screen, GREEN, (y * BLOCK_SIZE, x * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        
        pygame.display.update()




    
