import pygame
import random
import math

class Labyrinth : 

    def __init__ (self, SIZE, style) :
        self.matrix = []
        self.destroy = True
        self.size = SIZE
        self.TOTAL_WALLS = 0
        self.destroy_interval = int(200 / 1.05 ** self.size)
        self.max_walls_to_destroy = int(self.size // 2) 
        self.check_chance = 1
        if style == "R" or style == "r" or style == "random" or style == "Random" :
            self.generateRandomMatrix()
        else :
            self.generateMatrix()

    def generateMatrix(self) :
        # that's the first line
        self.matrix = []
        self.matrix.append([0 for i in range(self.size)])    
        # this is the way into the maze
        self.matrix[0][1] = 1
        for i in range(1, self.size - 1) :
            self.matrix.append([])
            for j in range(self.size) :

                if j == 0 or j == self.size - 1 :
                    self.matrix[i].append(0)
                else :
                    if (i + j) % 2 == 0 :
                        self.matrix[i].append(1)
                    else :
                        self.matrix[i].append(0)
                        self.TOTAL_WALLS += 1

        self.matrix.append([0 for i in range(self.size)])    
        # this is the way out of the matrix
        self.matrix[self.size - 1][self.size - 2] = 1
    
    def generateRandomMatrix(self) :
        self.matrix.append([0 for i in range(self.size)])    
        # this is the way into the maze
        self.matrix[0][1] = 1
        for i in range(1, self.size - 1) :
            self.matrix.append([])
            for j in range(self.size) :

                if j == 0 or j == self.size - 1 :
                    self.matrix[i].append(0)
                else :
                    value = random.randint(0, 1)
                    self.matrix[i].append(value)
                    if value == 0 :
                        self.TOTAL_WALLS += 1

        self.matrix.append([0 for i in range(self.size)])    
        # this is the way out of the matrix
        self.matrix[self.size - 1][self.size - 2] = 1
    
    def getAdjacentCells(self, x, y) :
        points = []
        if x + 1 <= self.size - 1 :
            points.append((x + 1, y))
        if x - 1 >= 1 :
            points.append((x - 1, y))
        if y + 1 <= self.size - 1 :
            points.append((x, y + 1))
        if y - 1 >= 1 :
            points.append((x, y - 1))

        return points
    

    def destroyWalls(self) :
        # we destroy walls randomly 
        walls_to_destroy = random.randint(1, self.max_walls_to_destroy)
        walls_destroyed = 0
        chance = random.randint(1, 100)
        
        if chance > 40 and self.check_chance == 1:
            self.matrix[1][1] = 1
            self.matrix[self.size - 2][self.size - 2] = 1
            self.check_chance = 0
        if walls_to_destroy < self.TOTAL_WALLS :
            while walls_destroyed < walls_to_destroy :
                # coords of potential wall to remove
                x = random.randint(1, self.size - 2)
                y = random.randint(1, self.size - 2)

                if self.matrix[x][y] == 0 :
                    self.matrix[x][y] = 1
                    walls_destroyed += 1
            self.TOTAL_WALLS -= walls_destroyed

    def update(self) :
        #call the destroyWall method every 1s
        if pygame.time.get_ticks() % self.destroy_interval == 0 and self.destroy :
            self.destroyWalls()  
        pass
    
    def stopDestroyWalls(self) :
        self.destroy = False

    # this method is just for testing
    def printLabyrinth(self) :
        for i in self.matrix :
            for j in i :
                print(j, end=" ")
            print()
        print("\n\n\n")
