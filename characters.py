# from board import Board

class Characters:

    def __init__(self, char, height, width):
        self.height = height
        self.width = width
        self.char = char
        self.matrix = []
        self.x = 0
        self.y = 0

    def NewPosition(self, board, x, y):
        if board.checkbeforeplace(self, x, y) == 0:
            board.place(self, x, y)
            self.Position(x, y)
            return 0
        else:
            return 1

    def Position(self, x, y):
        self.x = x
        self.y = y

    def Up(self, board):
        if board.checkbeforeplace(self, self.x-1, self.y) == 0:
            board.place(self, self.x-1, self.y)
            self.Position(self.x-1, self.y)
        else:
            return 1
            
    def Right(self, board):
        if board.checkbeforeplace(self, self.x, self.y+1) == 0:
            board.place(self, self.x, self.y+1)
            self.Position(self.x, self.y+1)
        else:
            return 1
    
    def Left(self, board):
        if board.checkbeforeplace(self, self.x, self.y-1) == 0:
            board.place(self, self.x, self.y-1)
            self.Position(self.x, self.y-1)
        else:
            return 1

    def Down(self, board):
        if board.checkbeforeplace(self, self.x+1, self.y) == 0:
            # erase upper part
            board.place(self, self.x+1, self.y)
            self.Position(self.x+1, self.y)
        else:
            # print("error")
            return 1

    def Kill(self, board):
        self.matrix = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        board.place(board, self, self.x, self.y)

    # def returnMatrix(self):
    #     """Return person as a matrix."""
    #     return self.matrix

