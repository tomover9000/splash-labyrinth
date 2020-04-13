class Cell :
    def __init__(self, x, y, reachable) :
        self.x = x
        self.y = y
        self.parent = None
        self.g = 10000 
        self.h = 0
        self.f = 10000 
        self.reachable = reachable
    
    def printCell(self) :
        print(f"({self.parent.x},{self.parent.y})->({self.x},{self.y})")