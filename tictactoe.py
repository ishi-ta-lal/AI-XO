import sys
import pygame
import numpy as np
from constants import *


#PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption('AI-XO(XO)')
screen.fill( BG_COLOR )

class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS,COLS))
        print(self.squares)

class Game:
    
    def __init__(self):
        self.board = Board()
        self.showLines()
    
    def showLines(self):
        # vertical lines
        pygame.draw.line(screen, LINE_COLOR, (SQUARE, 0), (SQUARE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH-SQUARE, 0), (WIDTH-SQUARE, HEIGHT), LINE_WIDTH)
        
        # horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE), (WIDTH, SQUARE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT-SQUARE), (WIDTH, HEIGHT-SQUARE), LINE_WIDTH)

def main():
    
    game = Game()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

main()