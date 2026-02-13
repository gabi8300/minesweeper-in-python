# Minesweeper_in_Python
# Minesweeper (Python/Tkinter)

A desktop implementation of the Minesweeper game built with Python and the Tkinter library. This project uses an Object-Oriented Programming approach and features a modular, frame-based navigation system.

## Features

* *Difficulty Settings*: Choose between standard difficulty levels or create a custom board size.
* *Dynamic Board Generation*: Mines are randomly positioned on the board for every new round.
* *Countdown Timer*: If the time runs out, the game is lost.
* *Recursive Tile Clearing*: Clicking an empty tile automatically clears all adjacent empty or numbered tiles.
* *Flagging System*: Right-click to flag potential mines and protect yourself from accidental clicks.
* *Game State Popups*: Custom in-game overlays for winning or losing, with options to restart or change settings.


## Project Structure

The code is organized into modular files for easier maintenance:

* *minesweeper.py*: The entry point of the application.
* *app.py*: The main Application class that manages window logic, styling, and navigation.
* *game.py*: Contains the core Minesweeper logic, including board generation, win/loss conditions, and click events.
* *frames.py*: Defines the UI layouts for the Menu, Settings, Rules, and Game screens.
* *tile.py*: A custom widget class that represents individual board squares.
* *settings.py*: Holds difficulty constants and configuration limits.
* *assets/*: Directory containing image files.
