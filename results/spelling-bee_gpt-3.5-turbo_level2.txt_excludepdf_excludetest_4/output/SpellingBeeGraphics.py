# File: SpellingBeeGraphics.py

"""
This file implements the SpellingBeeGraphics class, which manages the
graphical display for the SpellingBee project.
"""

import atexit
import math
import tkinter

# Constants

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 300

BEEHIVE_X = 150                 # These constants specify the center
BEEHIVE_Y = 150                 # of the beehive figure

HEX_SIDE = 40                   # The length of a hexagon side
HEX_SEP = 76                    # The distance between hexagon centers

WORDLIST_X = 300                # Starting x coordinate of the wordlist
WORDLIST_Y = 20                 # Baseline of first word listed
WORDLIST_DX = 120               # Separation between wordlist columns
WORDLIST_DY = 17                # Separation between wordlist rows
WORDLIST_HEIGHT = 250           # Height of wordlist in pixels
MESSAGE_MARGIN = 15             # Distance from bottom to message area
DEFAULT_FIELD_SIZE = 10         # Number of characters in a default field

CENTER_HEX_COLOR = "#FFCC33"
OUTER_HEX_COLOR = "#DDDDDD"
CONTROL_STRIP_COLOR = "#EEEEEE"

LETTER_FONT = ("Helvetica Neue", -40, "bold")
WORDLIST_FONT = ("Helvetica Neue", -16, "normal")

# Derived constants

MESSAGE_Y = CANVAS_HEIGHT - MESSAGE_MARGIN

class SpellingBeeGraphics:
    """This class creates the SpellingBee window."""

    def __init__(self):
        """Creates the SpellingBee window."""

        def create_beehive():
            """Creates the beehive structure on the canvas."""
            x0 = BEEHIVE_X
            y0 = BEEHIVE_Y
            self._labels = [ add_hexagon(x0, y0, CENTER_HEX_COLOR) ]
            for k in range(6):
                theta = math.radians(30 + 60 * k)
                x = x0 + HEX_SEP * math.cos(theta)
                y = y0 - HEX_SEP * math.sin(theta)
                self._labels.append(add_hexagon(x, y, OUTER_HEX_COLOR))

        def add_hexagon(x0, y0, fill):
            """Adds a hexagon centered at (x0, y0) to the canvas."""
            coords = [ ]
            for i in range(6):
                theta = math.radians(180 - i * 60)
                x = x0 + HEX_SIDE * math.cos(theta)
                y = y0 - HEX_SIDE * math.sin(theta)
                coords += [ x, y ]
            self._canvas.create_polygon(*coords, width=1, fill=fill)
            return self._canvas.create_text(x0, y0,
                                            text="",
                                            font=LETTER_FONT)

        def create_message():
            """Creates the message area at the bottom of the canvas."""
            self._message = self._canvas.create_text(WORDLIST_X,
                                                     MESSAGE_Y,
                                                     text="",
                                                     anchor=tkinter.SW,
                                                     font=WORDLIST_FONT)

        def delete_window():
            """Closes the window and exits from the event loop."""
            self._tk.destroy()

        def start_event_loop():
            """Starts the tkinter event loop when the program exits."""
            self.event_loop()

        self._tk = tkinter.Tk()
        self._tk.title("SpellingBee")
        self._tk.protocol("WM_DELETE_WINDOW", delete_window)
        self._canvas = tkinter.Canvas(self._tk,
                                      bg="White",
                                      width=CANVAS_WIDTH,
                                      height=CANVAS_HEIGHT,
                                      highlightthickness=0)
        self._canvas.pack()
        self._controls = tkinter.Frame(self._tk,
                                       background=CONTROL_STRIP_COLOR)
        self._interactors = tkinter.Frame(self._controls)
        self._fields = { }
        self._wordlist = [ ]
        self._letters = ""
        self._wx = WORDLIST_X
        self._wy = WORDLIST_Y
        create_beehive()
        create_message()
        atexit.register(start_event_loop)

    def add_button(self, name, callback):
        """Adds a button to the control strip that calls callback."""

        def button_action():
            callback(name)

        padding = tkinter.Frame(self._interactors,
                                background=CONTROL_STRIP_COLOR,
                                padx=3, pady=6)
        padding.pack(side=tkinter.LEFT)
        border = tkinter.Frame(padding, background="Black", bd=1)
        border.pack()
        button = tkinter.Button(border,
                                text=name,
                                relief=tkinter.RAISED,
                                command=button_action)
        button.pack()


    def add_field(self, name, callback, nchars=DEFAULT_FIELD_SIZE):
        """Adds an input field to the control strip that calls callback."""

        def enter_action(text):
            callback(textvar.get())

        padding = tkinter.Frame(self._interactors,
                                background=CONTROL_STRIP_COLOR,
                                pady=6)
        padding.pack(side=tkinter.LEFT)
        label = tkinter.Label(padding,
                              background=CONTROL_STRIP_COLOR,
                              text=" " + name)
        label.pack()
        padding = tkinter.Frame(self._interactors,
                                background=CONTROL_STRIP_COLOR,
                                padx=3, pady=6)
        padding.pack(side=tkinter.LEFT)
        border = tkinter.Frame(padding, background="Black", bd=1)
        border.pack()
        textvar = tkinter.StringVar()
        entry = tkinter.Entry(border,
                              width=nchars,
                              relief=tkinter.FLAT,
                              textvariable=textvar,
                              highlightthickness=0)
        entry.bind("<Return>", enter_action)
        entry.pack()
        self._fields[name] = textvar

    def get_field(self, name):
        return self._fields[name].get()

    def set_field(self, name, value):
        return self._fields[name].set(value)

    def event_loop(self):
        """Displays the application and waits for events."""
        self._interactors.pack()
        self._controls.pack(expand=True, fill=tkinter.X)
        self._tk.mainloop()

    def set_beehive_letters(self, letters):
        """Updates the letters in the beehive."""
        if len(letters) != 7:
            raise ValueError("The letters argument must have seven letters.")
        self._letters = letters.upper()
        for i in range(7):
            self._canvas.itemconfigure(self._labels[i], text=self._letters[i])

    def get_beehive_letters(self):
        """Returns the letters in the beehive, all in uppercase."""
        return self._letters

    def clear_word_list(self):
        """Removes all words from the word list."""
        for id in self._wordlist:
            self._canvas.delete(id)
        self._wordlist.clear()
        self._wx = WORDLIST_X
        self._wy = WORDLIST_Y

    def add_word(self, word, color="Black"):
        """Adds a word to the word list and optionally sets its color."""
        id = self._canvas.create_text(self._wx,
                                      self._wy,
                                      text=word,
                                      anchor=tkinter.SW,
                                      font=WORDLIST_FONT,
                                      fill=color)
        self._wordlist.append(id)
        self._wy += WORDLIST_DY
        if self._wy > WORDLIST_Y + WORDLIST_HEIGHT:
            self._wx += WORDLIST_DX
            self._wy = WORDLIST_Y

    def show_message(self, msg, color="Black"):
        """Displays a message and optionally sets its color."""
        self._canvas.itemconfigure(self._message, text=msg, fill=color)
