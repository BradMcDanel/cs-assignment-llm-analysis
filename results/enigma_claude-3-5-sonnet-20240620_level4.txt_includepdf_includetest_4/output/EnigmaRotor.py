from EnigmaConstants import ALPHABET

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverse_permutation = self._invert_permutation(permutation)
        self._offset = 0

    def get_permutation(self):
        return self._permutation

    def get_inverse_permutation(self):
        return self._inverse_permutation

    def get_offset(self):
        return self._offset

    def get_visible_letter(self):
        return ALPHABET[self._offset]

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

    @staticmethod
    def _invert_permutation(permutation):
        return ''.join(ALPHABET[permutation.index(letter)] for letter in ALPHABET)

def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    new_index = ALPHABET.index(permutation[shifted_index])
    return (new_index - offset) % 26