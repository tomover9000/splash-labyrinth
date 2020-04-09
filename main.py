import pygame
from labyrinth import Labyrinth
from maze import Game
import sys

# globals 
SIZE = 70 
def main() :
    
    pygame.display.init()
    game = Game(SIZE)
    game.run()
    pygame.display.quit()
    sys.exit()

if __name__ == "__main__" :
    main()