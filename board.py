from BoardElements import Space
from mario import Mario
import os

class Board:
    def __init__(self, height, width):
        #Defining board
        self.height = height #24
        self.width = width #400
        self.dheight = 34
        self.frame_width = 92
        self.matrix = [[' ' for a in range(width)] for b in range(height)]
        self.score = 0

    def checkbeforeplace(self, element, x, y):
        Xi = element.x
        Yi = element.y
        if Xi is not None:
            for i in range(Xi, Xi+element.height):
                for j in range(Yi, Yi+element.width):
                    self.matrix[i][j] = ' '

        for i in range(x, x+element.height):
            for j in range(y, y+element.width):
                if j <= 396 and i <= 396:
                    if self.matrix[i][j] != ' ':
                        self.place(element, Xi, Yi)
                        return 1
        return 0

    def place(self, element, x, y):
        # print(element.__class__, element.width, element.matrix[0][0])
        if element.__class__ != Space:
            row = 0
            col = 0
            for i in range(x, x + element.height):
                for j in range(y, y + element.width):
                    self.matrix[i][j] = element.matrix[row][col]
                    col += 1
                row += 1
                col = 0
        else:
            row = 0
            col = 0
            for i in range(x, x + element.height):
                for j in range(y, y + element.width):
                    self.matrix[i][j] = ' '
                    col += 1
                row += 1
                col = 0

        self.editBoard(self.matrix)

    def editBoard(self, newMatrix):
        self.matrix = newMatrix   

    def returnStringBoard(self, Mario):
        stringBoard = ""
        displacement = Mario.FindDx(self, Mario.y)
        ranges = (displacement, displacement + 92)
        if displacement < 0:
            ranges = (400 - 92, 400)

        for x in range(self.dheight):
            for y in range(ranges[0], ranges[1]):
                try:
                    stringBoard += self.matrix[x][y]
                except IndexError:
                    print("You Win!")
            stringBoard += '\n'
        
        stringBoard += "Displacement: {} {} {}\n".format(displacement,Mario.x,Mario.y)
        stringBoard += "SCORE: " + str(self.score) + "\n"
        stringBoard += "LIVES: " + str(Mario.lives) + "\n"
        stringBoard += "Press 'q' to exit\n"
        return stringBoard
    
    # def stringBoard(self, Mario)
