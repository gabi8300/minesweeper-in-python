import tkinter as tk
from frames import MainFrame, FormFrame, RulesFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title("Minesweeper")
        self.geometry('600x500+300+30')
        self.resizable(False, False)
        self.frames = {}

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.add_frames()
        self.configure_buttons()

    def add_frames(self):
        main_frame = MainFrame(self)
        main_frame.grid(column=0, row=0, sticky="nsew")
        self.frames['main_frame'] = main_frame

        form_frame = FormFrame(self)
        form_frame.grid(column=0, row=0, sticky="nsew")
        self.frames['form_frame'] = form_frame

        rules_frame = RulesFrame(self)
        rules_frame.grid(column=0, row=0, sticky="nsew")
        self.frames['rules_frame'] = rules_frame

        main_frame.tkraise()

    def configure_buttons(self):
        goto_form = lambda: self.frames['form_frame'].tkraise()
        self.frames['main_frame'].winfo_children()[0].configure(command=goto_form)

        goto_rules = lambda: self.frames['rules_frame'].tkraise()
        self.frames['main_frame'].winfo_children()[1].configure(command=goto_rules)

        quit_game = lambda: self.frames['main_frame'].quit()
        self.frames['main_frame'].winfo_children()[2].configure(command=quit_game)