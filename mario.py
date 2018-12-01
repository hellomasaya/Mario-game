import sys, os, subprocess
from characters import Characters
# from board import Board
#mario cannot go out of window!!!!!!!!!!!!!!!!!!
class Mario(Characters):
    def __init__(self, char, height, width):
        Characters.__init__(self, char, height, width)
        self.matrix = [['(', '^', '^', ')'], ['/', ']', '[', '\\']]
        # self.char = "Mario"
        self.height = height
        self.width = width
        self.lives = 3
        self.dx = 0

    def FindDx(self, board, y):
        if self.y <= board.frame_width//2:
            self.dx = 0
        elif self.y >= 354:
            self.dx = self.y - 400
        else:
            self.dx = self.y - (board.frame_width//2)
        return self.dx

    def checkDeath(self, enemy, pit1, pit2, board):
        for e in enemy:
            if (self.y == e.y+4 or self.y+4 == e.y) and (self.x == e.x or self.x == e.x+1 or self.x==e.x-1):
                self.lives -= 1
                self.NewPosition(board,26,1)
        for p in pit1:
            if (self.y == p.y) and (self.x+2 == p.x):
                self.lives -= 1
                self.NewPosition(board,26,1)
        for p2 in pit2:
            if (self.y == p2.y) and (self.x+2 == p2.x):
                self.lives -= 1
                self.NewPosition(board,26,1)
        if self.lives == 0:
            self.destroy(board)

    def destroy(self, board):
        self.matrix = [['(', 'X', 'X', ')'], [' ', ']', '[', ' ']]
        board.place (self, self.x, self.y)
        os.system('clear')
        subprocess.Popen(['osascript', './stopscript'])

        print(board.returnStringBoard(self))
        print("SORRY, YOU HAVE DIED.\nGAME OVER\n")
        sys.exit()