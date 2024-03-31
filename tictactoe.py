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
        self.empty_sqrs = self.squares  
        self.marked_sqrs = 0  
        
    def finalState(self):
        #vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]
             
        #vertical wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0]
            
        #descending diagnol
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[1][1]
        
        #ascending diagnol
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            return self.squares[1][1]
        
        #no win
        return 0
        
        
    def markSquare(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1
        
    def emptySquare(self, row, col):
        return self.squares[row][col] == 0
    
    def getEmptySquares(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.emptySquare(row, col):
                    empty_sqrs.append((row, col))
         
        return empty_sqrs    
    
    def isFUll(self):
        return self.marked_sqrs == 9
    
    def isEmpty(self):
        return self.marked_sqrs == 0

class Game:
    
    def __init__(self):
        self.board = Board()
        # self.ai = AI()
        self.player = 1
        self.gamemode = 'pvp' #pvp or ai
        self.running = True
        self.showLines()
    
    def showLines(self):
        # vertical lines
        pygame.draw.line(screen, LINE_COLOR, (SQUARE, 0), (SQUARE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH-SQUARE, 0), (WIDTH-SQUARE, HEIGHT), LINE_WIDTH)
        
        # horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE), (WIDTH, SQUARE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT-SQUARE), (WIDTH, HEIGHT-SQUARE), LINE_WIDTH)

    def drawFig(self, row, col):
        if self.player == 1:
            #draw cross
            # desc line
            start_desc = (col * SQUARE + OFFSET, row * SQUARE + OFFSET)
            end_desc = (col * SQUARE + SQUARE - OFFSET, row * SQUARE + SQUARE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

            # asc line
            start_asc = (col * SQUARE + OFFSET, row * SQUARE + SQUARE - OFFSET)
            end_asc = (col * SQUARE + SQUARE - OFFSET, row * SQUARE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
            
        elif self.player == 2:
            #draw circle
            center = (col * SQUARE + SQUARE // 2, row * SQUARE + SQUARE // 2)
            pygame.draw.circle(screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)
    
    def nextTurn(self):
        self.player = self.player % 2 + 1
    
def main():
    
    game = Game()
    board = game.board
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQUARE
                col = pos[0] // SQUARE
                
                if board.emptySquare(row, col):
                    board.markSquare(row, col, game.player)
                    game.drawFig(row, col)
                    game.nextTurn() 
                           
        pygame.display.update()

main()