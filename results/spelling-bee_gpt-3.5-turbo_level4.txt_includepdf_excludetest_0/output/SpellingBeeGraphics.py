import atexit
import math
import tkinter

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 300

BEEHIVE_X = 150
BEEHIVE_Y = 150
HEX_SIDE = 40
HEX_SEP = 76
WORDLIST_X = 300
WORDLIST_Y = 20
WORDLIST_DX = 120
WORDLIST_DY = 17
WORDLIST_HEIGHT = 250
MESSAGE_MARGIN = 15
DEFAULT_FIELD_SIZE = 10

CENTER_HEX_COLOR = "#FFCC33"
OUTER_HEX_COLOR = "#DDDDDD"
CONTROL_STRIP_COLOR = "#EEEEEE"

LETTER_FONT = ("Helvetica Neue", -40, "bold")
WORDLIST_FONT = ("Helvetica Neue", -16, "normal")

MESSAGE_Y = CANVAS_HEIGHT - MESSAGE_MARGIN

class SpellingBeeGraphics:
    
    def __init__(self):

        def create_beehive():
            ...
        
        def add_hexagon(x0, y0, fill):
            ...
        
        def create_message():
            ...

        def delete_window():
            ...

        def start_event_loop():
            ...

        self._tk = tkinter.Tk()
        self._tk.title("SpellingBee")
        self._tk.protocol("WM_DELETE_WINDOW", delete_window)
        self._canvas = tkinter.Canvas(self._tk, bg="White", width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0)
        self._canvas.pack()
        self._controls = tkinter.Frame(self._tk, background=CONTROL_STRIP_COLOR)
        self._interactors = tkinter.Frame(self._controls)
        self._fields = {}
        self._wordlist = []
        self._letters = ""
        self._wx = WORDLIST_X
        self._wy = WORDLIST_Y
        create_beehive()
        create_message()
        atexit.register(start_event_loop())

    def add_button(self, name, callback):
        ...

    def add_field(self, name, callback, nchars=DEFAULT_FIELD_SIZE):
        ...

    def get_field(self, name):
        ...

    def set_field(self, name, value):
        ...

    def event_loop(self):
        ...

    def set_beehive_letters(self, letters):
        ...

    def get_beehive_letters(self):
        ...

    def clear_word_list(self):
        ...

    def add_word(self, word, color="Black"):
        ...

    def show_message(self, msg, color="Black"):
        ...

### SpellingBee.py ###
from SpellingBeeGraphics import SpellingBeeGraphics

DICTIONARY_FILE = "EnglishWords.txt"

def spelling_bee():

    def puzzle_action(s):
        ...

    def solve_action(s):
        ...

    sbg = SpellingBeeGraphics()
    sbg.add_field("Puzzle", puzzle_action)
    sbg.add_button("Solve", solve_action)

if __name__ == "__main__":
    spelling_bee()