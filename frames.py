import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from settings import *

class MyFrame(ttk.Frame, ABC):
    ROWS = 1
    COLS = 1

    @abstractmethod
    def add_widgets(self):
        print("Add widgets to the frame!")

    def configure_grid(self, padx=0, pady=0):
        self.rowconfigure(0, weight=1)
        for i in range(self.ROWS):
            self.rowconfigure(i+1, weight=0, pad=pady)
        self.rowconfigure(self.ROWS+1, weight=1)

        self.columnconfigure(0, weight=1)
        for i in range(self.COLS):
            self.columnconfigure(i+1, weight=0, pad=padx)
        self.columnconfigure(self.COLS+1, weight=1)

class MenuFrame(MyFrame):
    ROWS = 3

    def __init__(self, container):
        super().__init__(container)
        self.configure_grid(pady=50)

        self.style = ttk.Style()
        self.style.configure(
            "Menu.TButton", 
            font=('Bahnschrift', 17),
            padding=(40, 5)
        )
        
        self.add_widgets()

    def add_widgets(self):
        for i, text in enumerate(["New Game", "Rules", "Exit"]):
            ttk.Button(
                self, 
                text=text, 
                style="Menu.TButton"
            ).grid(column=1, row=i+1)

class SettingsFrame(MyFrame):
    ROWS = 7
    COLS = 4

    def __init__(self, container):
        super().__init__(container)
        self.configure_grid(50, 30)

        self.difficulty = tk.StringVar()
        self.parameters = [tk.IntVar(), tk.IntVar(), tk.IntVar()]
        self.timer = tk.IntVar()

        self.add_widgets()

    def add_widgets(self):
        for i, text in enumerate(["Height", "Width", "Mines"]):
            ttk.Label(self, text=text).grid(column=i+2, row=1)

        for i, dict in enumerate(difficulties.items()):
            radio = ttk.Radiobutton(
                self, 
                text=dict[0], 
                value=dict[0], 
                variable=self.difficulty
            )
            radio.grid(column=1, row=i+2, sticky="w")

            for j, val in enumerate(dict[1]):
                ttk.Label(self, text=str(val)).grid(column=j+2, row=i+2)

        radio = ttk.Radiobutton(
            self, 
            text="Custom", 
            value="Custom", 
            variable=self.difficulty
        )
        radio.grid(column=1, row=5, sticky="w")
        
        for i, vals in enumerate(custom_limits.values()):
            spinbox = ttk.Spinbox(
                self, 
                from_=vals[0], 
                to=vals[1], 
                textvariable=self.parameters[i], 
                width=5
            )
            spinbox.grid(column=i+2, row=5, pady=15)

        ttk.Label(self, text='Timer').grid(column=1, row=6)
        ttk.Spinbox(
            self, 
            from_=0, 
            to=1800, 
            textvariable=self.timer, 
            width=5
        ).grid(column=2, row=6)
        ttk.Label(self, text="seconds").grid(column=3, row=6)

        start_btn = ttk.Button(self, text="Start")
        start_btn.grid(column=2, row=self.ROWS, columnspan=2, pady=10)

        ttk.Button(self, text="Back").place(x=20, y=20)

    def reset_settings(self):
        self.difficulty.set("")
        self.timer.set(0)
        for param in self.parameters:
            param.set(0)

class RulesFrame(MyFrame):
    def __init__(self, container):
        super().__init__(container)
        self.add_widgets()

    def add_widgets(self):
        rules = tk.Text(
            self, 
            borderwidth=10, 
            relief="sunken", 
            padx=30, 
            pady=30,
            font = ('Bahnschrift', 12)
        )
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
    ROWS = 2

    def __init__(self, container):
        super().__init__(container)
        self.configure_grid()

        self.timer_frame = ttk.Frame(self, borderwidth=10, relief='sunken')
        self.board_frame = ttk.Frame(self)
        self.add_widgets()

    def add_widgets(self):
        self.timer_frame.grid(column=1, row=1, pady=10)
        self.board_frame.grid(column=1, row=2)

class PopupFrame(MyFrame):
    ROWS = 4

    def __init__(self, container, text=""):
        super().__init__(
            container, 
            padding=(100, 10),
            borderwidth=10,
            relief="ridge"
        )
        self.text = text

        self.configure_grid()
        self.add_widgets()

    def add_widgets(self):
        ttk.Label(self, text=self.text)
        ttk.Button(self, text="New settings")
        ttk.Button(self, text="Keep settings")
        ttk.Button(self, text="Quit")

        for i, widget in enumerate(self.winfo_children()):
            widget.grid(column=1, row=i+1, pady=15)