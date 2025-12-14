import tkinter as tk
from frames import MainFrame, FormFrame, RulesFrame, GameFrame
from game import Game
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title("Minesweeper")
        self.geometry('1000x600+300+30')
        self.frames = {}

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.add_frames()
        self.configure_buttons()

    def add_frames(self):
        self.frames.update({'main_frame': MainFrame(self),
                            'form_frame': FormFrame(self),
                            'rules_frame': RulesFrame(self),
                            'game_frame': GameFrame(self)})

        for frame in self.frames.values():
            frame.grid(column=0, row=0, sticky="nsew")

        self.frames['main_frame'].tkraise()

    def configure_buttons(self):
        goto_form = lambda: self.frames['form_frame'].tkraise()
        self.frames['main_frame'].winfo_children()[0].configure(command=goto_form)

        goto_rules = lambda: self.frames['rules_frame'].tkraise()
        self.frames['main_frame'].winfo_children()[1].configure(command=goto_rules)

        quit_game = lambda: self.frames['main_frame'].quit()
        self.frames['main_frame'].winfo_children()[2].configure(command=quit_game)

        self.frames['form_frame'].winfo_children()[-2].configure(command=self.configure_game)

        goto_main = lambda: self.frames['main_frame'].tkraise()
        self.frames['form_frame'].winfo_children()[-1].configure(command=goto_main)
        self.frames['rules_frame'].winfo_children()[-1].configure(command=goto_main)

    def configure_game(self):
        diff = str(self.frames['form_frame'].difficulty.get())
        params = self.frames['form_frame'].parameters

        if diff != "":
            if diff != "Custom":
                for i in range(3):
                    params[i].set(FormFrame.difficulties[diff][i])
            self.game = Game(self.frames['game_frame'].board_frame, 
                         params[0].get(),
                         params[1].get(),
                         params[2].get())
            self.frames['game_frame'].tkraise()
        else:
            showinfo(title='Error', message="You didn't choose a difficulty!")
        