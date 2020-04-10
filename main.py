import pygame
from labyrinth import Labyrinth
from maze import Game

# globals 
SIZE = 30 
def main() :
    print("Player 1 use Space \n Player 2 use Right Arrow")
    SIZE = int(input("Insert Playing size: ")) 
    DISPLAY_SIZE = int(input("Insert display size (marimea laturii patratului ferestrei): "))
    play_style = input("Game mode: (R)andom/(G)rid: ")
    pygame.display.init()
    game = Game(SIZE, DISPLAY_SIZE, play_style)
    game.run()
    pygame.display.quit()

if __name__ == "__main__" :
    main()