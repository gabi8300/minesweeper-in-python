import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class Cell(tk.Button):
    def __init__(self, container, value=0):
        super().__init__(container)
        self.value = value
        self.status = "hidden"
        self.set_image("assets/hidden.png")
        self.bind('<Button-1>', self.right_click)
        self.bind('<Button-3>', self.left_click)

    def right_click(self, event):
        if self.status == "hidden":
            self.change_stats(self.value, "visible")

    def left_click(self, event):
        if self.status == "hidden":
            self.change_stats("flag", "flagged")
        elif self.status == "flagged":
            self.change_stats("hidden", "hidden")

    def change_stats(self, image, new_status):
        self.set_image(f"assets/{image}.png")
        self.status = new_status

    def set_image(self, image):
        self.image = tk.PhotoImage(file=image)
        self.config(image=self.image)