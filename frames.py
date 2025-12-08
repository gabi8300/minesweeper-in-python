import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

class MyFrame(ttk.Frame, ABC):
    ROWS = 3
    COLS = 3

    @abstractmethod
    def add_widgets(self):
        print("Add widgets to the frame!")

    def configure_grid(self):
        self.rowconfigure(0, weight=1)
        for i in range(self.ROWS):
            self.rowconfigure(i+1, weight=0)
        self.rowconfigure(self.ROWS+1, weight=1)

        self.columnconfigure(0, weight=1)
        for i in range(self.COLS):
            self.columnconfigure(i+1, weight=0)
        self.columnconfigure(self.COLS+1, weight=1)

class MainFrame(MyFrame):
    COLS = 1

    def __init__(self, container):
        super().__init__(container)
        self.configure_grid()
        self.add_widgets()

    def add_widgets(self):
        for i, text in enumerate(["New Game", "Rules", "Exit"]):
            ttk.Button(self, text=text).grid(column=1, row=i+1, pady=20)

class FormFrame(MyFrame):
    ROWS = 6
    COLS = 5
    difficulties = {"Begginer": [9, 9, 10],
                    "Medium": [16, 16, 40],
                    "Expert": [16, 30, 99]}
    custom_limits = {"Height": [5, 16],
                     "Width": [8, 30],
                     "Mines": [10, 480]}

    def __init__(self, container):
        super().__init__(container)
        self.configure_grid()
        self.add_widgets()

    def add_widgets(self):
        for i, text in enumerate(["Height", "Width", "Mines"]):
            ttk.Label(self, text=text).grid(column=i+3, row=1)

        for i, dict in enumerate(self.difficulties.items()):
            ttk.Label(self, text=dict[0]).grid(column=2, row=i+2)
            for j, val in enumerate(dict[1]):
                ttk.Label(self, text=str(val)).grid(column=j+3, row=i+2)

        ttk.Label(self, text="Custom").grid(column=2, row=5)
        for i, vals in enumerate(self.custom_limits.values()):
            ttk.Spinbox(self, from_=vals[0], to=vals[1], width=5)
            self.winfo_children()[-1].grid(column=i+3, row=5, pady=15)

        start_btn = ttk.Button(self, text="Start")
        start_btn.grid(column=3, row=self.ROWS, columnspan=2, pady=10)

        ttk.Button(self, text="Back").place(x=20, y=20)

class RulesFrame(MyFrame):
    def __init__(self, container):
        super().__init__(container)
        self.add_widgets()

    def add_widgets(self):
        rules = tk.Text(self, borderwidth=0)
        rules.insert(index=1.0, chars=RulesFrame.get_rules())
        rules.config(state="disabled")
        rules.pack(padx=20, pady=70, fill="both", expand=True)

        ttk.Button(self, text="Back").place(x=20, y=20)

    @staticmethod
    def get_rules():
        with open("utils/rules.txt", "r") as file:
            content = file.read()
        return content

class GameFrame(MyFrame):
    def __init__(self, container):
        super().__init__(container)
        self.configure_grid()
        self.add_widgets()

    def add_widgets(self):
        pass