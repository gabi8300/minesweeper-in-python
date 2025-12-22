import tkinter as tk
from tkinter import ttk
from frames import MenuFrame, SettingsFrame, RulesFrame, GameFrame
from game import Game
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title("Minesweeper")
        self.geometry('1000x600+130+20')
        self.font = ('Bahnschrift', 12)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.add_frames()
        self.configure_buttons()

        self.style = ttk.Style()
        self.style.configure('TButton', font=self.font)
        self.style.configure('TLabel', font=self.font)
        self.style.configure('TRadiobutton', font=self.font)

    def add_frames(self):
        self.frames = ({'menu': MenuFrame(self),
                        'settings': SettingsFrame(self),
                        'rules': RulesFrame(self),
                        'game': GameFrame(self)})

        for frame in self.frames.values():
            frame.grid(column=0, row=0, sticky="nsew")

        self.frames['menu'].tkraise()

    def configure_buttons(self):
        goto_settings = lambda: self.frames['settings'].tkraise()
        self.frames['menu'].winfo_children()[0].configure(command=goto_settings)

        goto_rules = lambda: self.frames['rules'].tkraise()
        self.frames['menu'].winfo_children()[1].configure(command=goto_rules)

        quit_game = lambda: self.frames['menu'].quit()
        self.frames['menu'].winfo_children()[2].configure(command=quit_game)

        self.frames['settings'].winfo_children()[-2].configure(command=self.configure_game)

        goto_menu = lambda: self.frames['menu'].tkraise()
        self.frames['settings'].winfo_children()[-1].configure(command=goto_menu)
        self.frames['rules'].winfo_children()[-1].configure(command=goto_menu)

    def configure_game(self):
        diff = str(self.frames['settings'].difficulty.get())
        params = self.frames['settings'].parameters
        timer = self.frames['settings'].timer.get()

        size = params[0].get() * params[1].get()

        if diff == "":
            showinfo(title='Error', message="You didn't choose a difficulty!")
        elif diff == "Custom" and \
            not ( 5 <= params[0].get() <= 16 and \
             8 <= params[1].get() <= 30 and \
             0.10 * size <= params[2].get() <= 0.75 * size):
                showinfo(title='Error', message="Parameters out of bounds!")
        else:
            if diff != "Custom":
                for i in range(3):
                    params[i].set(SettingsFrame.difficulties[diff][i])
            self.create_new_game(
                        params[0].get(),
                        params[1].get(),
                        params[2].get(),
                        timer)
            self.frames['settings'].reset_settings()

        goto_settings = lambda: self.frames['settings'].tkraise()
        self.game.popup.winfo_children()[1].configure(command=goto_settings)

        keep_settings = lambda: self.create_new_game(
                        params[0].get(),
                        params[1].get(),
                        params[2].get(),
                        timer)
        self.game.popup.winfo_children()[2].configure(command=keep_settings)

        goto_menu = lambda: self.frames['menu'].tkraise()
        self.game.popup.winfo_children()[3].configure(command=goto_menu)

    def create_new_game(self, height, width, mines, my_time):
        self.game = Game(self.frames['game'].board_frame,
                         height,
                         width,
                         mines)
        self.cronometer = ttk.Label(self.frames['game'].timer_frame, text="")
        self.cronometer.grid(column=0, row=0)
        self.update_timer(my_time)

        self.frames['game'].tkraise()

    def update_timer(self, my_time):
        if my_time >= 0:
            minutes = my_time // 60
            seconds = my_time % 60
            self.cronometer['text'] = f"{minutes:02}:{seconds:02}"
            self.after(1000, self.update_timer, my_time-1)