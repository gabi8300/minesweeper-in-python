import tkinter as tk
from tkinter import ttk

class Cell(tk.Button):
    def __init__(self, container, value=0, condition="hidden"):
        super().__init__(container, width=3)
        self.condition = condition
        self.value = value
        self.image = tk.PhotoImage(file="assets/hidden_cell.png")