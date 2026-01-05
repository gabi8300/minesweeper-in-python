import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from frames import *
from game import Game
from settings import difficulties

class App(tk.Tk):
    """ Represents the main window of the app"""

    def __init__(self):
        """Initializes the main window of the app"""
        super().__init__()
    
        self.title("Minesweeper")
        self.geometry('1000x600+130+20')
        self.font = ('Bahnschrift', 12)
        self.round = None

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.add_frames()
        self.configure_buttons()

        self.style = ttk.Style()
        self.style.configure('TButton', font=self.font)
        self.style.configure('TLabel', font=self.font)
        self.style.configure('TRadiobutton', font=self.font)

    def add_frames(self):
        """Adds all the frames of the app"""
        self.menu = MenuFrame(self)
        self.menu.grid(column=0, row=0, sticky="nsew")

        self.settings = SettingsFrame(self)
        self.settings.grid(column=0, row=0, sticky="nsew")

        self.rules = RulesFrame(self)
        self.rules.grid(column=0, row=0, sticky="nsew")

        self.game = GameFrame(self)
        self.game.grid(column=0, row=0, sticky="nsew")

        self.menu.tkraise()

    def configure_buttons(self):
        """Adds functionality to the buttons of the frames"""
        menu_buttons = self.menu.winfo_children()
        menu_buttons[0].configure(command=self.settings.tkraise)
        menu_buttons[1].configure(command=self.rules.tkraise)
        menu_buttons[2].configure(command=self.menu.quit)

        settings_buttons = self.settings.winfo_children()
        settings_buttons[-1].configure(command=self.menu.tkraise)
        self.rules.winfo_children()[-1].configure(command=self.menu.tkraise)

        settings_buttons[-2].configure(command=self.configure_game)

    def configure_game(self):
        """
        Validates the parameters set by the use and starts a new round
        """
        diff = str(self.settings.difficulty.get())

        try:
            params = list(map(lambda p: p.get(), self.settings.parameters))
            timer = self.settings.timer.get()
        except Exception as e:
            showinfo(title='Error', message="Parameters must be numbers!")
            print(e)

        if diff == "":
            showinfo(title='Error', message="You didn't choose a difficulty!")
        elif timer < 0 or timer > 1800:
            showinfo(title='Error', message="Timer must be in [0, 1800]!")
        elif diff == "Custom" and App.check_custom(*params):
            showinfo(title='Error', message="Parameters out of bounds!")
        else:
            if diff != "Custom":
                params = [difficulties[diff][i] for i in range(3)]
            self.create_new_round(*params, timer)

    def create_new_round(self, height, width, mines, timer):
        """
        Creates a new game round

        Args:
            height (int): board's height
            width (int): board's width
            mines (int): the number of mines
            timer (int): timer seconds
        """
        self.round = Game(
            self.game.board_frame,
            height, width, mines
        )

        popup_buttons = self.round.popup.winfo_children()
        popup_buttons[1].configure(command=self.new_settings)
        keep_settings = lambda: self.create_new_round(height, width, mines, timer)
        popup_buttons[2].configure(command=keep_settings)
        popup_buttons[3].configure(command=self.quit_round)

        self.cronometer = ttk.Label(self.game.timer_frame, text="")
        self.cronometer.grid(column=0, row=0)
        self.update_timer(timer)

        self.game.tkraise()

    def update_timer(self, timer):
        """
        Updates the timer of a round  every second

        Args:
            timer (int): timer seconds
        """
        if timer >= 0 and self.round.is_running:
            minutes = timer // 60
            seconds = timer % 60
            self.cronometer['text'] = f"{minutes:02}:{seconds:02}"
            self.after(1000, self.update_timer, timer-1)
        elif timer < 0:
            self.round.end_game("lost")

    def new_settings(self):
        """Resets game settings and redirects to the settings menu"""
        self.round.clear_board()
        self.cronometer['text'] = ""
        self.round = None
        self.settings.reset_settings()
        self.update_idletasks()
        self.settings.tkraise()

    def quit_round(self):
        """Exits the round and redirects to the main menu"""
        self.round.clear_board()
        self.cronometer['text'] = ""
        self.round = None
        self.settings.reset_settings()
        self.update_idletasks()
        self.menu.tkraise()

    @staticmethod
    def check_custom(height, width, mines):
        """
        Validates the given parameters

        Args:
            height (int): board's height
            width (int): board's width
            mines (int): number of mines

        Returns:
            bool: True/False
        """
        size = height * width
        return not (
            5 <= height <= 16 and \
            5 <= width <= 30 and \
            int(0.10 * size) <= mines <= int(0.75 * size)
        )
