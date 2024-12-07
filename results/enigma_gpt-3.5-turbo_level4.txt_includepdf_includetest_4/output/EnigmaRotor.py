from EnigmaConstants import ALPHABET

class EnigmaRotor:

    def __init__(self, permutation):
        self._permutation = permutation
        self._offset = 0

    def get_current_letter(self):
        return self._permutation[self._offset]

    def advance(self):
        self._offset = (self._offset + 1) % len(ALPHABET)