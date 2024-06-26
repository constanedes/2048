import os
import sys
import tkinter as tk
import constants as c
from enum import Enum
from classes import GameOverFrame, MainFrame, ScoreHeaderFrame
from tkinter import Menu, messagebox

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Directions(Enum):
    Up = 0
    Down = 1
    Right = 2
    Left = 3


class Game(tk.Tk):
    """Game root window"""

    def __init__(self) -> None:
        super().__init__()
        # Define root window settings
        self.grid()
        self.title(c.TITLE)
        self.wm_iconbitmap(resource_path(c.ICON_PATH))
        self.minsize(500, 500)
        self.resizable(False, False)

        # Menu settings
        self.menu = self.__create_menu()
        self.config(menu=self.menu)

        # Frame intializations
        self.score_header_frame = ScoreHeaderFrame(self)
        self.main_frame = MainFrame(self, self.score_header_frame)

        # Key bindings
        self.bind("<Left>", lambda _: self.__handle_binding(Directions.Left))
        self.bind("<Right>", lambda _: self.__handle_binding(Directions.Right))
        self.bind("<Up>", lambda _: self.__handle_binding(Directions.Up))
        self.bind("<Down>", lambda _: self.__handle_binding(Directions.Down))

        self.mainloop()

    def __create_menu(self) -> Menu:
        """Create menu items"""
        main_menu = Menu()

        options = Menu(main_menu, tearoff=0)
        options.add_command(
            label="Records"
        )
        options.add_separator()
        options.add_command(label="Exit", command=self.destroy)
        main_menu.add_cascade(label="Options", menu=options)

        help = Menu(main_menu, tearoff=0)
        help.add_command(
            label="Instructions",
            command=lambda: self.__show_message(c.INSTRUCTIONS, "Instructions")
        )
        help.add_command(
            label="About...",
            command=lambda: self.__show_message(c.ABOUT, "About"),
        )
        main_menu.add_cascade(label="Help", menu=help)
        return main_menu

    def __show_message(self, text: str, title: str):
         messagebox.showinfo(message=text, title=title)


    def __handle_binding(self, key: Directions) -> None:
        """Handles key bindings"""
        if self.__render_game_over_alert() is not None:
            return

        if key is Directions.Up:
            self.__up()
        elif key is Directions.Down:
            self.__down()
        elif key is Directions.Right:
            self.__right()
        elif key is Directions.Left:
            self.__left()

        self.main_frame.add_new_tile()
        self.main_frame.update_board()
        self.__render_game_over_alert()

    def __left(self) -> None:
        self.main_frame.stack()
        self.main_frame.combine()
        self.main_frame.stack()

    def __right(self) -> None:
        self.main_frame.reverse()
        self.main_frame.stack()
        self.main_frame.combine()
        self.main_frame.stack()
        self.main_frame.reverse()

    def __up(self) -> None:
        self.main_frame.transpose()
        self.main_frame.stack()
        self.main_frame.combine()
        self.main_frame.stack()
        self.main_frame.transpose()

    def __down(self) -> None:
        self.main_frame.transpose()
        self.main_frame.reverse()
        self.main_frame.stack()
        self.main_frame.combine()
        self.main_frame.stack()
        self.main_frame.reverse()

    def __render_game_over_alert(self) -> bool:
        """Shows game over modal"""
        status = self.main_frame.check_is_winner()
        if status is not None:
            text = "¡You Win!" if status is True else "You Lose... Try Again."
            GameOverFrame(self, text, False)
        return status


if __name__ == "__main__":
    print("Game starting...")
    Game()
