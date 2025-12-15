from cell import Cell
import random

class Game():
    def __init__(self, container, height = 9, width = 9, mines = 10):
        self.container = container
        self.height = height
        self.width = width
        self.mines = mines

        self.board = []
        self.make_board()
        self.add_mines()

    def make_board(self):
        for i in range(self.height):
            self.board.append([])
            for j in range(self.width):
                self.board[i].append(Cell(self.container))
                self.board[i][j].grid(column=j, row=i)

    def add_mines(self):
        count = 0
        population = range(1, self.width * self.height + 1)
        positions = random.sample(population, self.mines)

        for i in range(self.height):
            for j in range(self.width):
                count+=1
                if count in positions:
                    self.board[i][j].value = "mine"
                    self.update_neighbours(i, j)

    def update_neighbours(self, i, j):
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if 0 <= x < self.height and 0 <= y < self.width:
                    value = self.board[x][y].value
                    if value != "mine":
                        self.board[x][y].value = str(int(value) + 1)