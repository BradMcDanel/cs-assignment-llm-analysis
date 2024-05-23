import pytest
from unittest.mock import MagicMock, patch
import SpellingBee
from SpellingBeeGraphics import SpellingBeeGraphics

class MockSpellingBeeGraphics:
    def __init__(self):
        self.fields = {"Puzzle": "", "Word": ""}
        self.words = []
        self.messages = []

    def add_button(self, name, callback):
        self.button_callback = callback

    def add_field(self, name, callback):
        self.field_callback = callback

    def get_field(self, name):
        return self.fields.get(name, "")

    def set_field(self, name, value):
        self.fields[name] = value

    def get_beehive_letters(self):
        return self.fields["Puzzle"]

    def set_beehive_letters(self, letters):
        self.fields["Puzzle"] = letters

    def clear_word_list(self):
        self.words = []

    def add_word(self, word, color="Black"):
        self.words.append((word, color))

    def show_message(self, msg, color="Black"):
        self.messages.append((msg, color))

@pytest.fixture
def mock_graphics(monkeypatch):
    mock_graphics = MockSpellingBeeGraphics()
    monkeypatch.setattr(SpellingBee, 'SpellingBeeGraphics', lambda: mock_graphics)
    return mock_graphics

def test_puzzle_action(mock_graphics):
    print("Starting test_puzzle_action")
    sbg = mock_graphics
    SpellingBee.spelling_bee()

    sbg.set_field("Puzzle", "abcdefg")
    sbg.field_callback("abcdefg")

    print("Beehive letters:", sbg.get_beehive_letters())
    print("Messages:", sbg.messages)
    assert sbg.get_beehive_letters() == "abcdefg"
    assert not any("Invalid" in msg for msg, _ in sbg.messages)

def test_invalid_puzzle_length(mock_graphics):
    print("Starting test_invalid_puzzle_length")
    sbg = mock_graphics
    SpellingBee.spelling_bee()

    sbg.set_field("Puzzle", "abcde")
    sbg.field_callback("abcde")

    print("Messages:", sbg.messages)
    assert any("Invalid puzzle" in msg or "Not in the dictionary." in msg for msg, _ in sbg.messages)

def test_invalid_puzzle_duplicates(mock_graphics):
    print("Starting test_invalid_puzzle_duplicates")
    sbg = mock_graphics
    SpellingBee.spelling_bee()

    sbg.set_field("Puzzle", "abcdeff")
    sbg.field_callback("abcdeff")

    print("Messages:", sbg.messages)
    assert any("Invalid puzzle" in msg or "Not in the dictionary." in msg for msg, _ in sbg.messages)

def test_solve_action(mock_graphics):
    print("Starting test_solve_action")
    sbg = mock_graphics
    SpellingBee.spelling_bee()

    sbg.set_field("Puzzle", "abcdefg")
    sbg.field_callback("abcdefg")
    sbg.button_callback("Solve")

    print("Words:", sbg.words)
    print("Messages:", sbg.messages)
    assert len(sbg.words) > 0  # Check that words are found and displayed
    assert any("Found" in msg for msg, _ in sbg.messages)  # Check that the message shows the number of words and total score

def test_word_action(mock_graphics):
    print("Starting test_word_action")
    sbg = mock_graphics
    SpellingBee.spelling_bee()

    sbg.set_field("Puzzle", "abcdefg")
    sbg.field_callback("abcdefg")
    sbg.set_field("Word", "face")
    sbg.field_callback("face")

    print("Words:", sbg.words)
    print("Messages:", sbg.messages)
    assert any("face" in word for word, _ in sbg.words)  # Check that the word "face" is correctly added
    assert any("Found" in msg for msg, _ in sbg.messages)  # Check that the message shows the number of words and total score

if __name__ == "__main__":
    pytest.main()

