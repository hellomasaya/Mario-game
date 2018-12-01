import sys
from characters import Characters
from random import randint, random
from colorama import init, Fore, Back, Style
# from board import Board

class Enemy(Characters):
    def __init__(self, char, height, width):
        Characters.__init__(self, char, height, width)
        self.smart = (random() > 0.9)
        line = Fore.BLUE + '|' + Fore.RESET      
        arrow = Fore.MAGENTA + '^' + Fore.RESET      
        dash = Fore.WHITE + '_' + Fore.RESET
        if self.smart:
            line = Fore.CYAN + '|' + Fore.RESET      
            arrow = Fore.YELLOW + '^' + Fore.RESET      
            dash = Fore.WHITE + '_' + Fore.RESET
        self.matrix = [[line,arrow,arrow,line], [dash,line,line,dash]]
        self.height = height
        self.width = width
        self.destroyed = False

    def move(self, board, direction):
        if self.destroyed is True:
            return
        if direction == 1:
            while self.Left(board) != 1:
                direction = 1
                return
        else:
            while self.Right(board) != 1:
                direction = 2
                return

    def randomMove(self, board, mario):
        if (self.smart):
            if(mario.y < self.y):
                self.move(board, 1)
            else:
                self.move(board, 2)
        else:
            random_direction = randint(1, 2)
            self.move(board, random_direction)

    def addEnemy(self, board):
        placed = 0
        while placed == 0:
            x = randint(26,28)
            y = 4 * randint(5, 90)
            if board.checkbeforeplace(self, x, y) == 0:
                board.place(self, x, y)
                placed = 1
                self.x = x
                self.y = y

    def checkKill(self, superMario, board):
        if (superMario.y == self.y or superMario.y == self.y+1 or superMario.y == self.y+2 or superMario.y == self.y+3 or superMario.y == self.y-1 or superMario.y == self.y-2 or superMario.y == self.y-3) and (superMario.x+2== self.x):
            self.destroy(board)
            return True
        return False
            # board.score+=100
    
    def destroy(self, board):
        self.matrix = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        board.place(self, self.x, self.y)
        if self.destroyed is False:
            board.score += 100
            self.destroyed = True