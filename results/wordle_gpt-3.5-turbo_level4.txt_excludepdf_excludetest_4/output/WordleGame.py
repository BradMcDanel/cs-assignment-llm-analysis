import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow

class WordleGame:
    def __init__(self):
        self.hidden_word = random.choice(FIVE_LETTER_WORDS)
        self.guesses = []
        self.current_row = 0

    def check_word(self, word):
        if word in FIVE_LETTER_WORDS:
            return True
        else:
            return False

    def color_boxes(self, guess, gw):
        correct_letters = sum(guess[i] == self.hidden_word[i] for i in range(5))
        present_letters = len(set(guess) & set(self.hidden_word)) - correct_letters

        for i in range(5):
            if guess[i] == self.hidden_word[i]:
                gw.set_square_color(self.current_row, i, WordleGWindow.CORRECT_COLOR)
            elif guess[i] in self.hidden_word:
                gw.set_square_color(self.current_row, i, WordleGWindow.PRESENT_COLOR)
            else:
                gw.set_square_color(self.current_row, i, WordleGWindow.MISSING_COLOR)

        self.current_row += 1

    def play_game(self):
        gw = WordleGWindow()
        gw.set_current_row(self.current_row)

        def enter_action(s):
            if self.check_word(s):
                self.guesses.append(s)
                self.color_boxes(s, gw)
            else:
                gw.show_message("Not in word list")

        gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    game = WordleGame()
    game.play_game()