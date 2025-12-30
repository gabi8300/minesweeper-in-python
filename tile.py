import tkinter as tk

class Tile(tk.Button):
    def __init__(self, container, value=0):
        super().__init__(container)
        self.value = value
        self.status = "hidden"
        
        self.image = tk.PhotoImage(file="assets/hidden.png")
        self.config(image=self.image)
