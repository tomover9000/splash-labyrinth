#!/usr/bin/env python3

import pygame
import heapq
import random
from labyrinth import Labyrinth
from cell import Cell
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
        pygame.time.Clock().tick(10)
        self.Lab = Labyrinth(size, style)
        # this var keeps track of winners situation
        # 0 means the game is still running
        # 1 means p1 wins, 2 means p2 wins
        # 3 means the player who pushed the button lost
        self.winner = 0


    def genCells(self) : 
        self.cells = []
        for i in range(self.Lab.size) :
            for j in range(self.Lab.size) :
                self.cells.append(Cell(i, j, bool(self.Lab.matrix[i][j])))
               
        

    def input(self):
        events = pygame.event.get()

        for event in events :
            if event.type == KEYDOWN :
                if event.key == K_RIGHT :
                    self.Astar()

                #     if self.bfs(0, 1) :
                #         self.winner = 2
                #     else:
                #         self.winner = 0

                # if event.key == K_SPACE :
                #     if self.bfs(0, 1) == True :
                #         self.winner = 1
                #     else:
                #         self.winner = 3
                
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


    def Astar(self) :
        self.genCells()
        self.start = self.cells[1]
        self.end = self.cells[-2]
        # add start point to open Q
        Q_closed = []
        Q_open = []
        self.start.f = self.getHeuristic(self.start)
        Q_open.append(self.start)
        while len(Q_open) :
            # pop cell with lowest f
            current = self.getLowest(Q_open) 
            Q_open.remove(current)
            # add cell to closed Q
            Q_closed.append(current)
            self.displayPath(current, False)
            if current is self.end :
                # display path
                self.displayPath(current, True)
                print("We done")
                return True
            # get vecini
            adj_cells = self.getAdjacentCells(current)
            for adj_cell in adj_cells :
                if adj_cell.reachable and adj_cell not in Q_closed :
                    temp_g = current.g + 1
                    if adj_cell in Q_open :
                        if adj_cell.g > temp_g :
                            self.updateCell(adj_cell, current)
                    else :
                        # add cell to open list
                        self.updateCell(adj_cell, current)
                        Q_open.append(adj_cell)
            
        self.displayPath(current, True)
        return False
    



    def getHeuristic(self, cell) :
        return abs(self.end.x - cell.x) + abs(self.end.y - cell.y)
    
    def getLowest(self, l) :
        lowest = l[0]
        for i in l :
            if i.f < lowest.f :
                lowest = i
        return lowest
    
    def getCell(self, x, y) :
        return self.cells[x * self.Lab.size + y]
    
    def getAdjacentCells(self, cell) :
        vecini = [] 
        if cell.x < self.Lab.size - 1 :
            vecini.append(self.getCell(cell.x + 1, cell.y))
        if cell.y > 0 :
            vecini.append(self.getCell(cell.x, cell.y - 1))
        if cell.x > 0 :
            vecini.append(self.getCell(cell.x - 1, cell.y))
        if cell.y < self.Lab.size - 1 :
            vecini.append(self.getCell(cell.x, cell.y + 1))
        return vecini


    def updateCell(self, adj, cell) :
        adj.g = cell.g + 1
        adj.h = self.getHeuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def displayPath(self, end, isLast) :
        path = []
        prev_m = self.Lab.matrix
        cell = end
        while cell is not self.start :
            path.append(cell)
            self.Lab.matrix[cell.x][cell.y] = 3
            cell = cell.parent
        path.append(cell)
        self.Lab.matrix[cell.x][cell.y] = 3
        if pygame.time.get_ticks() % 2 == 0 :
            self.draw()
        if not isLast :
            if end != self.end :
                for i in path :
                    self.Lab.matrix[i.x][i.y] = 1
            if pygame.time.get_ticks() % 2 == 0 :
                self.draw()

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
                        pygame.draw.rect(self.screen, RED, (y * self.BLOCK_SIZE, x * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE))
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




    
