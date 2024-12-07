def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    new_index = ord(permutation[shifted_index]) - ord('A')
    return (new_index - offset) % 26

class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverse_permutation = self._invert_key(permutation)
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

    @staticmethod
    def _invert_key(key):
        inverse = [''] * 26
        for i, char in enumerate(key):
            inverse[ord(char) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)