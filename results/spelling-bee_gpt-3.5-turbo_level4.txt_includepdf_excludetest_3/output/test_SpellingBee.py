import pytest
from unittest.mock import MagicMock
import SpellingBee
from SpellingBeeGraphics import SpellingBeeGraphics

class MockSpellingBeeGraphics:
    def __init__(self):
        self.fields = {}
        self.beehive_letters = ""
        self.words = []
        self.messages = []

    def add_button(self, name, callback):
        setattr(self, f"{name.lower()}_callback", callback)

    def add_field(self, name, callback):
        self.fields[name] = ""
        setattr(self, f"{name.lower()}_callback", callback)

    def get_field(self, name):
        return self.fields.get(name, "")

    def set_field(self, name, value):
        self.fields[name] = value

    def get_beehive_letters(self):
        return self.beehive_letters

    def set_beehive_letters(self, letters):
        self.beehive_letters = letters

    def clear_word_list(self):
        self.words = []

    def add_word(self, word, color="Black"):
        self.words.append((word, color))

    def show_message(self, msg, color="Black"):
        self.messages.append((msg, color))

@pytest.fixture
def mock_graphics(monkeypatch):
    mock = MockSpellingBeeGraphics()
    monkeypatch.setattr(SpellingBee, 'SpellingBeeGraphics', lambda: mock)
    SpellingBee.spelling_bee()
    return mock

def test_puzzle_initialization(mock_graphics):
    mock_graphics.puzzle_callback("ABCDEFG")
    assert mock_graphics.get_beehive_letters() == "ABCDEFG"
    assert len(mock_graphics.messages) > 0  # Any message is fine

def test_invalid_puzzle_length(mock_graphics):
    mock_graphics.puzzle_callback("ABCDEF")
    assert mock_graphics.get_beehive_letters() != "ABCDEF"
    assert len(mock_graphics.messages) > 0  # Any error message is fine

def test_invalid_puzzle_duplicates(mock_graphics):
    mock_graphics.puzzle_callback("ABCDEFF")
    assert mock_graphics.get_beehive_letters() != "ABCDEFF"
    assert len(mock_graphics.messages) > 0  # Any error message is fine

def test_solve_action(mock_graphics):
    mock_graphics.set_beehive_letters("LYCENTX")
    mock_graphics.solve_callback("Solve")
    assert len(mock_graphics.words) > 0
    assert any("(" in word[0] for word in mock_graphics.words)  # Check for score display
    assert len(mock_graphics.messages) > 0  # Check for summary message

def test_word_entry_valid(mock_graphics):
    mock_graphics.set_beehive_letters("LYCENTX")
    initial_word_count = len(mock_graphics.words)
    mock_graphics.word_callback("excel")
    assert len(mock_graphics.words) > initial_word_count
    assert any("excel" in word[0].lower() for word in mock_graphics.words)
    assert len(mock_graphics.messages) > 0  # Any message is fine

def test_word_entry_invalid(mock_graphics):
    mock_graphics.set_beehive_letters("LYCENTX")
    initial_word_count = len(mock_graphics.words)
    mock_graphics.word_callback("invalid")
    assert len(mock_graphics.words) == initial_word_count
    assert len(mock_graphics.messages) > 0  # Any error message is fine

def test_pangram_identification(mock_graphics):
    mock_graphics.set_beehive_letters("LYCENTX")
    mock_graphics.word_callback("excellently")
    assert any("excellently" in word[0].lower() and word[1] == "Blue" for word in mock_graphics.words)

def test_score_calculation(mock_graphics):
    mock_graphics.set_beehive_letters("LYCENTX")
    mock_graphics.word_callback("excel")
    mock_graphics.word_callback("excellently")
    assert any("(" in word[0] for word in mock_graphics.words)  # Check for score display
    assert len(mock_graphics.messages) > 0  # Check for score message

def test_duplicate_word_entry(mock_graphics):
    mock_graphics.set_beehive_letters("LYCENTX")
    mock_graphics.word_callback("excel")
    initial_word_count = len(mock_graphics.words)
    mock_graphics.word_callback("excel")
    assert len(mock_graphics.words) == initial_word_count
    assert len(mock_graphics.messages) > 0  # Any error message is fine

def test_solve_after_user_input(mock_graphics):
    mock_graphics.set_beehive_letters("LYCENTX")
    mock_graphics.word_callback("excel")
    initial_word_count = len(mock_graphics.words)
    mock_graphics.solve_callback("Solve")
    assert len(mock_graphics.words) > initial_word_count

if __name__ == "__main__":
    pytest.main()
