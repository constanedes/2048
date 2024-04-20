TITLE = "2048"
ICON_PATH = "./assets/game.ico"

GRID_COLOR = "#A39489"
EMPTY_CELL_COLOR = "#C2B3A9"

SCORE_LABEL_FONT = ("Verdana", 24)
SCORE_FONT = ("Helvetica", 34, "bold")

GAME_OVER_FONT = ("Helvetica", 38, "bold")
GAME_OVER_FONT_COLOR = "#F5F5F5"

WINNER_BG = "#FFCC00"
LOSER_BG = "#A39489"

CELL_COLORS = {
    2: "#fcefe6",
    4: "#f2e8cb",
    8: "#f5b682",
    16: "#f29446",
    32: "#ff775c",
    64: "#e64c2e",
    128: "#ede291",
    256: "#fce130",
    512: "#ffdb4a",
    1024: "#f0b922",
    2048: "#fad74d"
}

CELL_NUMBER_COLORS = {
    2: "#695C57",
    4: "#695C57",
    8: "#FFFFFF",
    16: "#FFFFFF",
    32: "#FFFFFF",
    64: "#FFFFFF",
    128: "#FFFFFF",
    256: "#FFFFFF",
    512: "#FFFFFF",
    1024: "#FFFFFF",
    2048: "#FFFFFF",
}

CELL_NUMBER_FONTS = {
    2: ("Helvetica", 55, "bold"),
    4: ("Helvetica", 55, "bold"),
    8: ("Helvetica", 55, "bold"),
    16: ("Helvetica", 50, "bold"),
    32: ("Helvetica", 50, "bold"),
    64: ("Helvetica", 50, "bold"),
    128: ("Helvetica", 45, "bold"),
    256: ("Helvetica", 45, "bold"),
    512: ("Helvetica", 45, "bold"),
    1024: ("Helvetica", 40, "bold"),
    2048: ("Helvetica", 40, "bold"),
}

INSTRUCTIONS = '''
Objective: The goal of the game is to create a tile with the number 2048.

How to Play: Use the arrow keys (Up, Down, Left, Right) to move the tiles.
Tiles with the same number merge into one when they touch.
With every move, a new tile with the number 2 or 4 appears randomly on an empty spot.

Winning: You win the game when you create a tile with the number 2048.
Losing: The game is over when there are no more moves possible, and the board is full.
'''

ABOUT = '''
2048 Game
Developed by Constantino Edes

© 2024 All rights reserved
Licensed under the MIT License.
'''