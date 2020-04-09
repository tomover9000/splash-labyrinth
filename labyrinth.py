import pygame
import random

class Labyrinth : 

    matrix = []

    def __init__ (self, SIZE) :
        # marimea asta include si peretii de la margini
        # gen
        # 0 0 0 0 0 0 0
        # 0 1 0 1 0 1 0
        # 0 0 1 0 1 0 0
        # 0 1 0 1 0 1 0
        # 0 0 1 0 1 0 0
        # 0 1 0 1 0 1 0
        # 0 0 0 0 0 0 0
        self.size = SIZE
        self.generateMatrix()


    def generateMatrix(self) :
        # that's the first line
        self.matrix.append([0 for i in range(self.size)])    
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

        self.matrix.append([0 for i in range(self.size)])    

    def destroyWalls(self) :
        # we destroy walls randomly 
        walls_to_destroy = random.randint(1, 10)
        walls_destroyed = 0
        while walls_destroyed < walls_to_destroy :
            # coords of potential wall to remove
            x = random.randint(1, self.size - 2)
            y = random.randint(1, self.size - 2)

            if self.matrix[x][y] == 0 :
                self.matrix[x][y] = 1
                walls_destroyed += 1

    def update(self) :
        # call the destroyWall method every 1s
        if pygame.time.get_ticks() % 200 == 0 :
            self.destroyWalls()  


    # this method is just for testing
    def printLabyrinth(self) :
        for i in self.matrix :
            for j in i :
                print(j, end=" ")
            print()
