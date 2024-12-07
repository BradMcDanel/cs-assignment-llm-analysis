def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    new_char = permutation[shifted_index]
    return (ord(new_char) - 65 - offset) % 26

def invert_key(key):
    inverted = [''] * 26
    for i, char in enumerate(key):
        inverted[ord(char) - 65] = chr(i + 65)
    return ''.join(inverted)

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverse_permutation = invert_key(permutation)
        self._offset = 0

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def get_inverse_permutation(self):
        return self._inverse_permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0