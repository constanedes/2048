import tkinter as tk
import constants as c
import random

class MainFrame(tk.Frame):
    def __init__(self, parent: tk.Tk, score_header_frame: tk.Frame) -> None:
        super().__init__(parent, bg=c.GRID_COLOR, height=600, width=600)
        self.grid(pady=(100, 0))

        self.score_header_frame = score_header_frame  
        self.__render_board()
        self.__insert_data()

    def start_game(self):
        self.__insert_data()
        self.__render_board()

    
    # Call ScoreHeaderFrame reference for update their score
    def __update_score(self):
        self.score_header_frame.update_score(self.score)  

    # Fills the cells for use in board
    def __render_board(self) -> None:
        self.cells = [
            [
                {
                    "frame": CellFrame(self, row=i, column=j), 
                    "number": CellNumberFrame(self, row=i, column=j)
                } for j in range(4)
            ] for i in range(4)
        ]

    # Inserts 2 or 4 inside de matrix
    def __insert_data(self) -> None:
        self.matrix = [[0] * 4 for _ in range(4)]
        for _ in range(2):
            while True:
                row = random.randint(0, 3)
                col = random.randint(0, 3)
                number = random.choice([2, 4])
                if self.matrix[row][col] == 0:
                    self.matrix[row][col] = number
                    break
            self.__insert_first_numbers(row, col, str(number))

        self.score = 0

    # Render the first widget data of the board
    def __insert_first_numbers(self, row: int, col: int, number: str) -> None:
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONTS[2],
            text=number,
        )

    def transpose(self):
        '''Transposes the matrix by swapping rows and columns'''
        self.matrix = [list(row) for row in zip(*self.matrix)]

    def reverse(self):
        '''Reverses the order of elements within rows'''
        self.matrix = [row[::-1] for row in self.matrix]

    def stack(self):
        '''Shifts non-zero elements towards the top of each column'''
        for col in range(4):
            stack_pointer = 0
            for row in range(4):
                if self.matrix[row][col] != 0:
                    self.matrix[stack_pointer][col] = self.matrix[row][col]
                    if stack_pointer != row:
                        self.matrix[row][col] = 0
                    stack_pointer += 1

    def combine(self):
        '''Combines adjacent equal elements within rows'''
        for row in range(4):
            for col in range(3):
                if self.matrix[row][col] == self.matrix[row][col + 1] and self.matrix[row][col] != 0:
                    self.matrix[row][col] *= 2
                    self.matrix[row][col + 1] = 0
                    self.score += self.matrix[row][col]

    def add_new_tile(self):
        '''Add new tile to the grid'''
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.matrix[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.matrix[row][col] = random.choice([2, 4])

    def update_board(self):
        '''Update the GUI to match the matrix'''
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(bg=c.EMPTY_CELL_COLOR, text="")
                else:
                    self.cells[i][j]["frame"].configure(bg=c.CELL_COLORS[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg=c.CELL_COLORS[cell_value],
                        fg=c.CELL_NUMBER_COLORS[cell_value],
                        font=c.CELL_NUMBER_FONTS[cell_value],
                        text=str(cell_value)
                    )
        self.__update_score()
        self.update_idletasks()

    # Check if no movements possible
    def __no_moves_possible(self) -> bool:
        horizontal_moves = any(self.matrix[i][j] == self.matrix[i][j + 1] for i in range(4) for j in range(3))
        vertical_moves = any(self.matrix[i][j] == self.matrix[i + 1][j] for i in range(3) for j in range(4))
        board_full = all(self.matrix[i][j] != 0 for i in range(4) for j in range(4))
        return not horizontal_moves and not vertical_moves and board_full

    def check_is_winner(self) -> bool:
        '''Check if is game over (Winner/Loser)'''
        if any(2048 in row for row in self.matrix):
            return True
        elif self.__no_moves_possible() is True:
            return False
        else:
            return None


class GameOverFrame(tk.Frame):
    def __init__(self, parent: tk.Widget, text: str, is_winner: bool) -> None:
        super().__init__(parent, borderwidth=2)
        self.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(
            self,
            text=text,
            bg=c.WINNER_BG if is_winner else c.LOSER_BG,  
            fg=c.GAME_OVER_FONT_COLOR, 
            font=c.GAME_OVER_FONT
        ).pack()


class CellFrame(tk.Frame):
    def __init__(self, parent, row, column) -> None:
        super().__init__(parent, bg=c.EMPTY_CELL_COLOR, height=150, width=150)
        self.grid(row=row, column=column, padx=5, pady=5)


class CellNumberFrame(tk.Label):
    def __init__(self, parent, row, column) -> None:
        super().__init__(parent, bg=c.EMPTY_CELL_COLOR)
        self.grid(row=row, column=column)


class ScoreHeaderFrame(tk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.place(relx=0.5, y=45, anchor="center")
        tk.Label(self, text="Score", font=c.SCORE_LABEL_FONT).grid(row=0)
        self.score = tk.Label(self, text="0", font=c.SCORE_FONT)
        self.score.grid(row=1)

    # Updates score number
    def update_score(self, new_score) -> None:
        self.score.config(text=str(new_score))