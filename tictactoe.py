import copy
import sys
import random
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
        
    def finalState(self, show=False):
        #vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = CIRCLE_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    iPos = (col * SQUARE + SQUARE // 2, 20)
                    fPos = (col * SQUARE + SQUARE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col]
             
        #vertical wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRCLE_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    iPos = (20, row * SQUARE + SQUARE // 2)
                    fPos = (WIDTH - 20, row * SQUARE + SQUARE // 2)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]
            
        #descending diagnol
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = CIRCLE_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, 20)
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]
        
        #ascending diagnol
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                color = CIRCLE_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, HEIGHT - 20)
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
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
    
    def isFull(self):
        return self.marked_sqrs == 9
    
    def isEmpty(self):
        return self.marked_sqrs == 0

class AI:
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player
        
    def rnd_choice(self, board):
        empty_sqrs = board.getEmptySquares()
        idx = random.randrange(0, len(empty_sqrs))
        
        return empty_sqrs[idx]
    
    def minmax(self,board, maximizing):
        # terminal cases
        case = board.finalState()
        
        # player 1 wins
        if case == 1:
            return 1, None # eval, move
        
        #player 2 wins
        if case == 2:
            return -1, None
        
        # draw
        elif board.isFull():
            return 0, None
        
        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.getEmptySquares()
            
            for (row,col) in empty_sqrs: # type: ignore
                temp_board = copy.deepcopy(board) 
                temp_board.markSquare(row, col, 1)
                eval = self.minmax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
                    
            return max_eval, best_move
         
        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.getEmptySquares()
            
            for (row,col) in empty_sqrs: # type: ignore
                temp_board = copy.deepcopy(board) 
                temp_board.markSquare(row, col, self.player)
                eval = self.minmax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)
                    
            return min_eval, best_move
        
    def eval(self, main_board):
        if self.level == 0:
            #random
            eval = 'random'
            move = self.rnd_choice(main_board)
        
        else:
            #minmax algo choice
            eval, move = self.minmax(main_board, False)    
        
        print(f'AI has chosen to mark the square in pos {move} with an eval of {eval}')
        return move

class Game:
    
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1
        self.gamemode = 'ai' #pvp or ai
        self.running = True
        self.showLines()
        
    def makeMove(self, row, col):
        self.board.markSquare(row, col, self.player)
        self.drawFig(row, col)
        self.nextTurn()
    
    def showLines(self):
        # fill bg
        screen.fill( BG_COLOR )
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
    
    def makeMove(self, row, col):
        self.board.markSquare(row, col, self.player)
        self.drawFig(row, col)
        self.nextTurn()

    def nextTurn(self):
        self.player = self.player % 2 + 1
        
    def changeGamemode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'
    
    def isover(self):
        return self.board.finalState(show = True) != 0 or self.board.isFull()
        
    def reset(self):
        self.__init__()
    
def main():
    
    game = Game()
    board = game.board
    ai = game.ai
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                
                # g - gamemode
                if event.key == pygame.K_g:
                    game.changeGamemode()
                    
                # r - reset
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai
                    
                # 0 - random ai
                if event.key == pygame.K_0:
                    ai.level = 0
                    
                # 1 - random ai
                if event.key == pygame.K_1:
                    ai.level = 1
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQUARE
                col = pos[0] // SQUARE
                
                if board.emptySquare(row, col) and game.running:
                    game.makeMove(row, col)
                    
                    if game.isover():
                        game.running = False
                                
        if game.gamemode == 'ai' and game.player == ai.player and game.running:
            pygame.display.update()
            
            #ai methods
            row, col = ai.eval(board)
            game.makeMove(row,col)
            
            if game.isover():
                game.running = False
            
        pygame.display.update()

main()