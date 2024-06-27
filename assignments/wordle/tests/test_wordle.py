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

def test_valid_guess(mock_window, set_target_word):
    set_target_word('apple')
    wordle()
    mock_window.enter_listeners[0]('apple'.upper())

    # Check for correct message
    for msg in mock_window.messages:
      if 'congratulations' in msg.lower():
          return
    assert False

def test_invalid_guess(mock_window, set_target_word):
    set_target_word('apple')
    wordle()
    mock_window.enter_listeners[0]('zzzzz'.upper())

    # Check for not in word list message
    for msg in mock_window.messages:
      if 'not in word list' in msg.lower():
          return
    assert False


def test_correct_color_update(mock_window, set_target_word):
    set_target_word('apple')
    wordle()
    mock_window.enter_listeners[0]('apple'.upper())

    # Check if all squares are correct color
    for i in range(5):
        assert mock_window.get_square_color(0, i) == CORRECT_COLOR

def test_present_and_missing_color_update(mock_window, set_target_word):
    set_target_word('apple')
    wordle()
    mock_window.enter_listeners[0]('ample'.upper())

    # Check colors
    assert mock_window.get_square_color(0, 0) == CORRECT_COLOR  # 'a' is correct
    assert mock_window.get_square_color(0, 1) == MISSING_COLOR  # 'm' is present
    assert mock_window.get_square_color(0, 2) == CORRECT_COLOR  # 'p' is correct
    assert mock_window.get_square_color(0, 3) == CORRECT_COLOR  # 'l' is correct
    assert mock_window.get_square_color(0, 4) == CORRECT_COLOR  # 'e' is correct
  
    
def test_game_over_condition(mock_window, set_target_word):
    set_target_word('apple')
    wordle()
    
    # Make six incorrect guesses
    for _ in range(6):
        mock_window.enter_listeners[0]('wrong'.upper())
    
    
    assert mock_window.get_current_row() == 5
    
    # Check for game over message
    for msg in mock_window.messages:
      if 'apple' in msg.lower():
          return
          
if __name__ == "__main__":
    pytest.main()

