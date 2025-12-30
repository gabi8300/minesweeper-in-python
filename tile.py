import tkinter as tk

class Tile(tk.Button):
    """Represents a tile"""
    def __init__(self, container, value=0):
        """
        Initializes the tile

        Args:
            container (Frame): the game board
            value (str): tile's value
        """
        super().__init__(container)
        self.value = value
        self.status = "hidden"
        
        self.image = tk.PhotoImage(file="assets/hidden.png")
        self.config(image=self.image)
