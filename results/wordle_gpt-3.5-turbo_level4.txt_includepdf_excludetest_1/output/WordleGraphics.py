"""
This file implements the WordleGWindow class, which manages the graphical display for the Wordle project.
"""

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

# Rest of the code provided as-is