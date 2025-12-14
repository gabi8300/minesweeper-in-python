from cell import Cell

class Game():
    def __init__(self, container, height = 9, width = 9, mines = 10):
        self.container = container
        self.height = height
        self.width = width
        self.mines = mines
        self.make_board()

    def make_board(self):
        for i in range(self.height):
            for j in range(self.width):
                Cell(self.container).grid(column=j, row=i)