from EnigmaConstants import ALPHABET

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverse_permutation = self._invert_permutation(permutation)
        self._offset = 0

    def _invert_permutation(self, permutation):
        return ''.join(sorted(permutation, key=lambda c: permutation.index(c)))

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

    def get_visible_letter(self):
        return ALPHABET[self._offset]

    def apply_forward(self, signal):
        shifted_signal = (signal + self._offset) % 26
        permuted_signal = ALPHABET.index(self._permutation[shifted_signal])
        return (permuted_signal - self._offset) % 26

    def apply_backward(self, signal):
        shifted_signal = (signal + self._offset) % 26
        permuted_signal = ALPHABET.index(self._inverse_permutation[shifted_signal])
        return (permuted_signal - self._offset) % 26