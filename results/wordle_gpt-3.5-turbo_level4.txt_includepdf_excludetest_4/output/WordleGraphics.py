import atexit
import math
import time
import tkinter

# Constants
N_ROWS = 6
N_COLS = 5
CORRECT_COLOR = "#66BB66"
PRESENT_COLOR = "#CCBB66"
MISSING_COLOR = "#999999"
UNKNOWN_COLOR = "#FFFFFF"
KEY_COLOR = "#DDDDDD"
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 700
SQUARE_SIZE = 60
SQUARE_SEP = 5
TOP_MARGIN = 30
BOTTOM_MARGIN = 30
MESSAGE_SEP = 20
SQUARE_FONT = ("Helvetica Neue", -44, "bold")
MESSAGE_FONT = ("Helvetica Neue", -20, "bold")
KEY_FONT = ("Helvetica Neue", -18)
ENTER_FONT = ("Helvetica Neue", -14)
KEY_WIDTH = 40
KEY_HEIGHT = 60
KEY_CORNER = 9
KEY_XSEP = 5
KEY_YSEP = 7
KEY_LABELS = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "DELETE"]
]
CLICK_MAX_DISTANCE = 2
CLICK_MAX_DELAY = 0.5
SQUARE_DELTA = SQUARE_SIZE + SQUARE_SEP
BOARD_WIDTH = N_COLS * SQUARE_SIZE + (N_COLS - 1) * SQUARE_SEP
BOARD_HEIGHT = N_ROWS * SQUARE_SIZE + (N_ROWS - 1) * SQUARE_SEP
MESSAGE_X = CANVAS_WIDTH / 2
MESSAGE_Y = TOP_MARGIN + BOARD_HEIGHT + MESSAGE_SEP

class WordleGWindow:
    def __init__(self):
        # Constructor code here

    def get_square_letter(self, row, col):
        return self._grid[row][col].get_letter()

    def set_square_letter(self, row, col, ch):
        self._grid[row][col].set_letter(ch)

    def get_square_color(self, row, col):
        return self._grid[row][col].get_color()

    def set_square_color(self, row, col, color):
        self._grid[row][col].set_color(color)

    def get_key_color(self, ch):
        return self._keys[ch].get_color()

    def set_key_color(self, ch, color):
        self._keys[ch].set_color(color)

    def get_current_row(self):
        return self._row

    def set_current_row(self, row):
        self._row = row
        self._col = 0
        for col in range(N_COLS):
            self.set_square_letter(row, col, " ")
            self.set_square_color(row, col, UNKNOWN_COLOR)

    def add_enter_listener(self, fn):
        self._enter_listeners.append(fn)

    def show_message(self, msg, color="Black"):
        self._message.set_text(msg, color)

class WordleSquare:
    def __init__(self, canvas, row, col):
        # Square initialization code here

    def get_letter(self):
        return self._ch

    def set_letter(self, ch):
        self._ch = ch
        self._canvas.itemconfigure(self._text, text=ch)

    def get_color(self):
        return self._color

    def set_color(self, color):
        color = color.upper()
        self._color = color
        fg = "White"
        if color == UNKNOWN_COLOR:
            fg = "Black"
        self._canvas.itemconfig(self._frame, fill=color)
        self._canvas.itemconfig(self._text, fill=fg)

class WordleKey:
    def __init__(self, canvas, x, y, width, height, label):
        # Key initialization code here

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color
        fg = "White"
        if color == UNKNOWN_COLOR:
            fg = "Black"
        self._canvas.itemconfig(self._frame, fill=color)
        self._canvas.itemconfig(self._text, fill=fg)

class WordleMessage:
    def __init__(self, canvas, x, y):
        # Message initialization code here

    def get_text(self):
        return self._text

    def set_text(self, text, color="Black"):
        self._text = text
        self._canvas.itemconfigure(self._msg, text=text, fill=color)