class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverse_permutation = self._invert_permutation(permutation)
        self._offset = 0

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

    def forward(self, index):
        return self._apply_permutation(index, self._permutation, self._offset)

    def backward(self, index):
        return self._apply_permutation(index, self._inverse_permutation, self._offset)

    def _apply_permutation(self, index, permutation, offset):
        shifted_index = (index + offset) % 26
        new_index = ord(permutation[shifted_index]) - 65
        return (new_index - offset) % 26

    def _invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            inverse[ord(char) - 65] = chr(i + 65)
        return ''.join(inverse)