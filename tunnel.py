from BoardElements import BoardElement
import random
from random import randint
from colorama import init, Fore, Back, Style


class Tunnel(BoardElement):

    def __init__(self, height, width):
        BoardElement.__init__(self, height, width) #3,5
        Tunn = Back.RED + Fore.BLACK + 'I' + Fore.RESET + Back.RESET
        self.matrix = [[Tunn for a in range(width)] for b in range(height)]

    def Position(self, x, y):
        self.x = x
        self.y = y

    def placeTunnel(self, board):
        occur = 0
        while occur == 0:
            x = 25#something is wronng!
            # y = 4 * random.choice(range(20, 350))
            y = randint(20,380)
            if board.checkbeforeplace(self, x, y) == 0:
                board.place(self, x, y)
                occur = 1
                self.Position(x,y)    


