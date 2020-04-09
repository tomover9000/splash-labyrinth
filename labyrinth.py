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
        size = SIZE + 2
        self.generateMatrix()


    def generateMatrix(self) :
        # that's the first line
        self.matrix.append([0 for i in range(size)])    
        for i in range(size - 2) :
            self.matrix.append([])
            for j in range(size - 2) :
                if (i + j) % 2 == 0 :
                    self.matrix[i].append(0)
                else :
                    self.matrix[i].append(1)

    def printLabyrinth(self) :
        for i in matrix :
            for j in matrix[i] :
                print(j, end="")
            print()
