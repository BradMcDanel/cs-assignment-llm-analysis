from EnigmaConstants import ALPHABET

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverse_permutation = self._invert_permutation(permutation)
        self._offset = 0

    def _invert_permutation(self, permutation):
        return ''.join(ALPHABET[permutation.index(letter)] for letter in ALPHABET)

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

    def apply_forward(self, index):
        shifted_index = (index + self._offset) % 26
        permuted_index = ALPHABET.index(self._permutation[shifted_index])
        return (permuted_index - self._offset) % 26

    def apply_backward(self, index):
        shifted_index = (index + self._offset) % 26
        permuted_index = ALPHABET.index(self._inverse_permutation[shifted_index])
        return (permuted_index - self._offset) % 26

def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    permuted_char = permutation[shifted_index]
    return (ALPHABET.index(permuted_char) - offset) % 26