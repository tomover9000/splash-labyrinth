#!/usr/bin/env python3

import pygame
import random
from labyrinth import Labyrinth
from pygame.locals import *
import sys

GRAY = (84, 84, 84)
SILVER = (194, 194, 194)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
BLUE = (0, 0, 255)


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
        # this var keeps track of winners situation
        # 0 means the game is still running
        # 1 means p1 wins, 2 means p2 wins
        # 3 means the player who pushed the button lost
        self.winner = 0
        

    def input(self):
        events = pygame.event.get()

        for event in events :
            if event.type == KEYDOWN :
                if event.key == K_RIGHT :
                    if self.solve(0, 1) :
                        self.winner = 2
                    else:
                        self.winner = 0

                if event.key == K_SPACE :
                    if self.solve(0, 1) == True :
                        self.winner = 1
                    else:
                        self.winner = 3
                
                if event.key == K_r :
                    self.Lab = Labyrinth(self.size, self.style)
                    self.winner = 0

            if event.type == QUIT :
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.Lab.stopDestroyWalls()
                if event.key == K_SPACE:
                    self.Lab.stopDestroyWalls()


    def bfs(self, start_x, start_y) :
        # coada 
        Q = []
        # mark start as discovered
        self.Lab.matrix[start_x][start_y] = 2
        # let's append tuples consisting of coords in maze
        Q.append((start_x, start_y))

        while len(Q) > 0 :
            current = Q.pop()
            if current.x == self.Lab.size - 1 and current.y == self.Lab.size - 1 :
                return True


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

        if self.winner == 0 :
            for x in range(self.Lab.size) :
                for y in range(self.Lab.size) :
                    if self.Lab.matrix[x][y] == 1 :
                        pygame.draw.rect(self.screen, WHITE, (y * self.BLOCK_SIZE, x * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE))
                    if self.Lab.matrix[x][y] == 2 :
                        pygame.draw.rect(self.screen, GRAY, (y * self.BLOCK_SIZE, x * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE))
                    if self.Lab.matrix[x][y] == 3 :
                        pygame.draw.rect(self.screen, SILVER, (y * self.BLOCK_SIZE, x * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE))
        elif self.winner == 1 :
            # winner player 1
            self.screen.fill(BLUE)
        elif self.winner == 2 :
            # winner player 2
            self.screen.fill(GREEN)
        elif self.winner == 3 :
            # loser
            self.screen.fill(RED)

        pygame.display.update()




    
