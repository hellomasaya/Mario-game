import random,sys
from random import randint
from colorama import init, Fore, Back, Style
# from board import Board

class BoardElement:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.matrix=[]
        self.x=0
        self.y=0

    def addelements(self, board, x1,x2,y1,y2): 
        for r in range(x1, x2, 2):  #28,34,2   #0,6,2
            for c in range(y1, y2, 4): #0,400,4  #204,400,4
                board.place(self, r, c)

class Space(BoardElement):

    def __init__(self, height, width):
        BoardElement.__init__(self, height, width)
        self.matrix = [" "]

class Platform(BoardElement):

    def __init__(self, height, width):
        BoardElement.__init__(self, height, width) 
        Plat = Back.RED + Fore.BLACK + 'I' + Fore.RESET + Back.RESET
        self.matrix = [[Plat, Plat, Plat, Plat], [Plat, Plat, Plat, Plat]]

class Pit(BoardElement):

    def __init__(self, height, width):
        BoardElement.__init__(self, height, width) 
        fire = Back.YELLOW + Fore.RED + '^' + Fore.RESET + Back.RESET
        self.matrix = [[' ', ' ', ' ', ' '], [fire,fire,fire,fire]]

    def addPit(self,board):
        occur = 0
        while occur == 0:
            x = 28#something is wronng!
            # y = 4 * random.choice(range(20, 350))
            y = randint(20,200)
            # if board.checkbeforeplace(self, x, y) == 0:
            board.place(self, x, y)
            occur = 1
            self.x=x
            self.y=y

class Pit2(BoardElement):

    def __init__(self, height, width):
        BoardElement.__init__(self, height, width) 
        fire = Back.GREEN + Fore.WHITE + '~' + Fore.RESET + Back.RESET
        self.matrix = [[' ', ' ', ' ', ' '], [fire,fire,fire,fire]]

    def addPit2(self,board):
        occur = 0
        while occur == 0:
            x = 28#something is wronng!
            # y = 4 * random.choice(range(20, 350))
            y = randint(204,380)
            # if board.checkbeforeplace(self, x, y) == 0:
            board.place(self, x, y)
            occur = 1
            self.x=x
            self.y=y

class Cloud(BoardElement):

    def __init__(self, height, width):
        BoardElement.__init__(self, height, width)
        shape = Back.GREEN + Fore.GREEN + '#' + Fore.RESET + Back.RESET
        self.matrix = [
            [' ', ' ',shape,shape,shape,shape,' '],
            [shape,shape,shape,shape,shape,shape,shape,],
            [' ', shape,shape,shape,shape,shape,' ']
        ]

    def addCloud(self, board):
            occur = 0
            while occur == 0:
                x = randint(2,3)#something is wronng!
                # y = 4 * random.choice(range(20, 350))
                y = randint(0,200)
                if board.checkbeforeplace(self, x, y) == 0:
                    board.place(self, x, y)
                    occur = 1
                    self.x=x
                    self.y=y

class Win(BoardElement):

    def __init__(self, height, width):
        BoardElement.__init__(self, height, width)
        shape = Back.YELLOW + Fore.YELLOW + '#' + Fore.RESET + Back.RESET
        y = Back.YELLOW + Fore.BLACK + 'Y' + Fore.RESET + Back.RESET
        o = Back.YELLOW + Fore.BLACK + 'O' + Fore.RESET + Back.RESET
        u = Back.YELLOW + Fore.BLACK + 'U' + Fore.RESET + Back.RESET
        w = Back.YELLOW + Fore.BLACK + 'W' + Fore.RESET + Back.RESET
        i = Back.YELLOW + Fore.BLACK + 'I' + Fore.RESET + Back.RESET
        n = Back.YELLOW + Fore.BLACK + 'N' + Fore.RESET + Back.RESET
        self.matrix = [
            [shape,shape,shape,shape,shape,shape,shape,shape],
            [shape,y,o,u,w,i,n,shape],
            [shape, shape,shape,shape,shape,shape,shape, shape]
        ]

    def youWin(self, board):
        occur = 0
        while occur == 0:
            x = 24#something is wronng!
            # y = 4 * random.choice(range(20, 350))
            y = 390
            if board.checkbeforeplace(self, x, y) == 0:
                board.place(self, x, y)
                occur = 1
                self.x=x
                self.y=y        

    def checkKill(self,superMario,board):
        if (superMario.y == self.y or superMario.y == self.y+1 or superMario.y == self.y+2 or superMario.y == self.y+3 or superMario.y == self.y-1 or superMario.y == self.y-2 or superMario.y == self.y-3 ) and (superMario.x== self.x+2 or superMario.x+2 == self.x):
            print("YOU WIN")          
            sys.exit()

