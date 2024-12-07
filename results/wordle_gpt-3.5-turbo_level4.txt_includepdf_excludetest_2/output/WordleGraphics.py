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

class WordleGWindow:
    def __init__(self):
        # Constructor code here

    def get_square_letter(self, row, col):
        pass

    def set_square_letter(self, row, col, ch):
        pass

    def get_square_color(self, row, col):
        pass

    def set_square_color(self, row, col, color):
        pass

    def get_key_color(self, ch):
        pass

    def set_key_color(self, ch, color):
        pass

    def get_current_row(self):
        pass

    def set_current_row(self, row):
        pass

    def add_enter_listener(self, fn):
        pass

    def show_message(self, msg, color="Black"):
        pass

class WordleSquare:
    def __init__(self, canvas, row, col):
        # Square initialization code

    def get_letter(self):
        pass

    def set_letter(self, ch):
        pass

    def get_color(self):
        pass

    def set_color(self, color):
        pass

class WordleKey:
    def __init__(self, canvas, x, y, width, height, label):
        # Key initialization code

    def get_color(self):
        pass

    def set_color(self, color):
        pass

class WordleMessage:
    def __init__(self, canvas, x, y):
        # Message initialization code

    def get_text(self):
        pass

    def set_text(self, text, color="Black"):
        pass