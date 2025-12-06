import tkinter as tk
from tkinter import ttk

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.rowconfigure(0, weight=1)
        for i in range(3):
            self.rowconfigure(i+1, weight=0)
        self.rowconfigure(4, weight=1)

        self.columnconfigure(0, weight=1)

        self.add_widgets()

    def add_widgets(self):
        ttk.Button(self, text="New Game")
        ttk.Button(self, text="Rules")
        ttk.Button(self, text="Exit")

        for i, btn in enumerate(self.winfo_children()):
            btn.grid(column=0, row=i+1, pady=20)

class FormFrame(ttk.Frame):
    ROWS = 4
    COLS = 2

    def __init__(self, container):
        super().__init__(container)

        self.rowconfigure(0, weight=1)
        for i in range(FormFrame.ROWS):
            self.rowconfigure(i+1, weight=0)
        self.rowconfigure(FormFrame.ROWS+1, weight=1)

        self.columnconfigure(0, weight=1)
        for i in range(FormFrame.COLS):
            self.columnconfigure(i+1, weight=0)
        self.columnconfigure(FormFrame.COLS+1, weight=1)

        self.add_widgets()

    def add_widgets(self):
        labels = []
        labels.append(ttk.Label(self, text="Rows:"))
        labels.append(ttk.Label(self, text="Cols:"))
        labels.append(ttk.Label(self, text="Mines:"))

        for i, label in enumerate(labels):
            label.grid(column=1, row=i+1)

        rows_value = tk.StringVar(value=9)
        cols_value = tk.StringVar(value=9)
        mines_value = tk.StringVar(value=10)

        inputs = []
        inputs.append(ttk.Spinbox(self, from_=5, to=16, textvariable=rows_value))
        inputs.append(ttk.Spinbox(self, from_=8, to=30, textvariable=cols_value))
        inputs.append(ttk.Spinbox(self, from_=10, to=480, textvariable=mines_value))

        for i, input in enumerate(inputs):
            input.grid(column=2, row=i+1, pady=15)

        start_btn = ttk.Button(self, text="Start")
        start_btn.grid(column=1, row=4, columnspan=2, pady=10)

class RulesFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.add_widgets()

    def add_widgets(self):
        rules = tk.Text(self, borderwidth=0) # relief="flat"
        rules.insert(index=1.0, chars=RulesFrame.get_rules())
        rules.config(state="disabled")
        rules.pack(padx=10, pady=10, fill="both", expand=True)

    @staticmethod
    def get_rules():
        with open("utils/rules.txt", "r") as file:
            content = file.read()
        return content
