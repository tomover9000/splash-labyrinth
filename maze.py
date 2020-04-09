#!/usr/bin/env python3

import pygame
import random
from labyrinth import Labyrinth
from pygame.locals import *
import sys

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)


class Game:


    def __init__(self, size, disp_size, style):

        self.disp_size = disp_size
        self.style = style
        self.BLOCK_SIZE = self.disp_size // size
        self.size = size
        self.screen = pygame.display.set_mode((self.disp_size, self.disp_size))
        pygame.display.set_caption('Splash Labyrinth')
        pygame.time.Clock().tick(60)
        self.Lab = Labyrinth(size, style)
        

    def input(self):
        events = pygame.event.get()

        for event in events :
            if event.type == KEYDOWN :
                if event.key == K_SPACE :
                    self.solve(0, 1)
                if event.key == K_r :
                    self.Lab = Labyrinth(self.size, self.style)
            if event.type == KEYUP :
                if event.key == K_SPACE :
                    self.Lab.stopDestroyWalls()
            if event.type == QUIT :
                sys.exit()

    def solve(self, x, y) :
        # marcam caile trecute cu 2
        self.draw()
        self.input()
        
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
                    pygame.draw.rect(self.screen, WHITE, (y * self.BLOCK_SIZE, x * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE))
                if self.Lab.matrix[x][y] == 2 :
                    pygame.draw.rect(self.screen, RED, (y * self.BLOCK_SIZE, x * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE))
                if self.Lab.matrix[x][y] == 3 :
                    pygame.draw.rect(self.screen, GREEN, (y * self.BLOCK_SIZE, x * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE))

        
        pygame.display.update()




    
