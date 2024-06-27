import pytest
from unittest.mock import MagicMock
import random
import Wordle
from WordleDictionary import FIVE_LETTER_WORDS
from Wordle import wordle, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

class MockWordleGWindow:
    def __init__(self):
        self.enter_listeners = []
        self.messages = []
        self.squares = [[{'letter': '', 'color': MISSING_COLOR} for _ in range(5)] for _ in range(6)]
        self.keys = {ch: {'color': MISSING_COLOR} for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        self.current_row = 0
        self.current_col = 0
        self._down_x = 0
        self._down_y = 0
        self._down_time = 0

    def add_enter_listener(self, fn):
        self.enter_listeners.append(fn)

    def show_message(self, msg, color="Black"):
        self.messages.append(msg)

    def get_square_letter(self, row, col):
        return self.squares[row][col]['letter']

    def set_square_letter(self, row, col, ch):
        self.squares[row][col]['letter'] = ch

    def get_square_color(self, row, col):
        return self.squares[row][col]['color']

    def set_square_color(self, row, col, color):
        self.squares[row][col]['color'] = color

    def get_key_color(self, ch):
        return self.keys[ch]['color']

    def set_key_color(self, ch, color):
        self.keys[ch]['color'] = color

    def get_current_row(self):
        return self.current_row

    def set_current_row(self, row):
        self.current_row = row
        self.current_col = 0
        for col in range(5):
            self.set_square_letter(row, col, " ")
            self.set_square_color(row, col, MISSING_COLOR)

    def press_action(self, tke):
        self._down_x = tke.x
        self._down_y = tke.y
        self._down_time = time.time()

    def release_action(self, tke):
        if abs(self._down_x - tke.x) <= 2:
            if abs(self._down_y - tke.y) <= 2:
                t = time.time()
                if t - self._down_time < 0.5:
                    key = self.find_key(tke.x, tke.y)
                    if key:
                        self.key_action(key)

    def key_action(self, key):
        ch = key.upper()
        if ch == "DELETE":
            self.show_message("")
            if self.current_row < 6 and self.current_col > 0:
                self.current_col -= 1
                self.set_square_letter(self.current_row, self.current_col, " ")
        elif ch == "ENTER":
            self.show_message("")
            s = ""
            for col in range(5):
                s += self.get_square_letter(self.current_row, col)
            for fn in self.enter_listeners:
                fn(s)
        elif ch.isalpha():
            self.show_message("")
            if self.current_row < 6 and self.current_col < 5:
                self.set_square_letter(self.current_row, self.current_col, ch)
                self.current_col += 1

    def find_key(self, x, y):
        # Mock find_key function for testing
        return "A"

    def start_event_loop(self):
        pass

    def delete_window(self):
        pass

@pytest.fixture
def mock_window(monkeypatch):
    mock_window = MockWordleGWindow()
    monkeypatch.setattr(Wordle, 'WordleGWindow', lambda: mock_window)
    return mock_window

@pytest.fixture
def set_target_word(monkeypatch):
    def _set_target_word(word):
        monkeypatch.setattr(random, 'choice', lambda _: word)
    return _set_target_word