import pygame
import random

class Labyrinth : 

    matrix = []

    def __init__ (self, SIZE) :
        # marimea asta include si peretii de la margini
        # gen
        # 0 1 0 0 0 0 0
        # 0 1 0 1 0 1 0
        # 0 0 1 0 1 0 0
        # 0 1 0 1 0 1 0
        # 0 0 1 0 1 0 0
        # 0 1 0 1 0 1 0
        # 0 0 0 0 0 1 0
        self.destroy = True
        self.size = SIZE
        self.generateMatrix()
        self.printLabyrinth()


    def generateMatrix(self) :
        # that's the first line
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
                    self.matrix[i].append(random.randint(0, 1))

        self.matrix.append([0 for i in range(self.size)])    
        # this is the way out of the matrix
        self.matrix[self.size - 1][self.size - 2] = 1
    

    def destroyWalls(self) :
        # we destroy walls randomly 
        walls_to_destroy = random.randint(1, 20)
        walls_destroyed = 0
        while walls_destroyed < walls_to_destroy :
            # coords of potential wall to remove
            x = random.randint(1, self.size - 2)
            y = random.randint(1, self.size - 2)

            if self.matrix[x][y] == 0 :
                self.matrix[x][y] = 1
                walls_destroyed += 1

    def update(self) :
        #call the destroyWall method every 1s
        if pygame.time.get_ticks() % 100 == 0 and self.destroy :
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
