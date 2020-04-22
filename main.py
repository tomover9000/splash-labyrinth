import pygame
from labyrinth import Labyrinth
from maze import Game

# globals 
SIZE = 30 
def main() :
    print("Player 1 use Space \nPlayer 2 use Right Arrow")
    SIZE = int(input("Insert Playing size (20 - 100): ")) 
    if SIZE < 20 :
        SIZE = 20
    if SIZE > 100 :
        SIZE = 100
    DISPLAY_SIZE = int(input("Insert display size (marimea laturii patratului ferestrei): "))
    play_style = input("Game mode: (R)andom/(G)rid: ")
    pygame.display.init()
    game = Game(SIZE, DISPLAY_SIZE, play_style)
    game.run()
    pygame.display.quit()

if __name__ == "__main__" :
    main()