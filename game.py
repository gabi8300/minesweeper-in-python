import tkinter as tk
from tkinter import ttk
from frames import PopupFrame
from tile import Tile
import random

class Game():
    def __init__(self, container, height, width, mines):
        self.container = container
        self.height = height
        self.width = width
        self.mines = mines

        self.popup = PopupFrame(self.container.master.master)
        self.popup.grid(column=0, row=0)

        self.make_board()
        self.add_mines()

    def make_board(self):
        self.board = []
        for i in range(self.height):
            self.board.append([])
            for j in range(self.width):
                self.board[i].append(Tile(self.container))
                self.board[i][j].grid(column=j, row=i)
                self.board[i][j].bind('<Button-1>', lambda event, x=i, y=j: self.right_click(event, x, y))
                self.board[i][j].bind('<Button-3>', Game.toggle_flag)

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

    def right_click(self, event, i, j):
        if event.widget.value == "mine":
            event.widget.config(bg="red")
            self.reveal_mines()
        else:
            self.reveal_tiles(i, j)

        result = self.check_win()
        if result in ("lost", "won"):
            self.popup.winfo_children()[0]['text'] = f"You {result}!"
            self.popup.tkraise()

    def reveal_mines(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j].value == "mine":
                    Game.change_status(self.board[i][j], "visible")

    def check_win(self):
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j].status == "visible":
                    if self.board[i][j].value == "mine":
                       return "lost"
                    else:
                        count+=1
        if count == (self.width * self.height) - self.mines:
            return "won"
        return "continue"


    def reveal_tiles(self, i, j):
        if int(self.board[i][j].value) > 0:
            Game.change_status(self.board[i][j], "visible")
        else:
            Game.change_status(self.board[i][j], "visible")
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if 0 <= x < self.height and 0 <= y < self.width \
                        and self.board[x][y].status == "hidden":
                            self.reveal_tiles(x, y)

    @staticmethod
    def toggle_flag(event):
        if event.widget.status == "hidden":
            Game.change_status(event.widget, "flagged")
        elif event.widget.status == "flagged":
            Game.change_status(event.widget, "hidden")

    @staticmethod
    def change_status(widget, status):
        if status == "visible":
            image = widget.value
        elif status == "flagged":
            image = "flag"
        else:
            image = "hidden"
            
        widget.image = tk.PhotoImage(file=f"assets/{image}.png")
        widget.config(image=widget.image)
        widget.status = status