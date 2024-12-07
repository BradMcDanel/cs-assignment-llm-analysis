class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._offset = 0

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0  # Returns True if a full revolution occurs

    def apply_permutation(self, index, offset):
        shifted_index = (index + offset) % 26
        translated_char = self._permutation[shifted_index]
        translated_index = (ALPHABET.index(translated_char) - offset) % 26
        return translated_index

def invert_key(permutation):
    inverse = [''] * 26
    for i, char in enumerate(permutation):
        inverse[ALPHABET.index(char)] = ALPHABET[i]
    return ''.join(inverse)