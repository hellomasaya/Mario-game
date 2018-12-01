from BoardElements import BoardElement
import random
from colorama import init, Fore, Back, Style


class Brick(BoardElement):

    def __init__(self, height, width):
        BoardElement.__init__(self, height, width) #2,4
        Bric = Fore.CYAN + '/' + Fore.RESET      
        self.matrix = [[Bric for a in range(width)] for b in range(height)]
        self.destroyed = False

    def placeBrick(self, board):
        occur = 0
        while occur == 0:
            x = random.choice(range(10, 24, 1)) #something is wronng!
            y = random.choice(range(20, 350, 4))
            # y = 5 * randint(1,15)
            if board.checkbeforeplace(self, x, y) == 0:
                board.place(self, x, y)
                occur = 1
                self.Position(x,y)   
                
    def Position(self, x, y):
        self.x = x
        self.y = y

    def checkKill(self,superMario,board):
        if (superMario.y == self.y or superMario.y == self.y+1 or superMario.y == self.y+2 or superMario.y == self.y+3 or superMario.y == self.y-1 or superMario.y == self.y-2 or superMario.y == self.y-3) and (superMario.x== self.x+2):
            self.destroy(board)
            return True
        return False
            # board.score+=50

    def destroy(self, board):
        self.matrix = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        board.place(self, self.x, self.y)
        if self.destroyed is False:
            board.score += 20
            self.destroyed = True