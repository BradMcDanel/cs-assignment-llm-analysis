class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._offset = 0
        self._inverse_permutation = self._invert_permutation(permutation)

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

    def _invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            inverse[ord(char) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)

    def apply_permutation(self, index, offset):
        shifted_index = (index + offset) % 26
        substituted_char = self._permutation[shifted_index]
        result_index = (ord(substituted_char) - ord('A') - offset) % 26
        return result_index

    def apply_inverse_permutation(self, index, offset):
        shifted_index = (index + offset) % 26
        substituted_char = self._inverse_permutation[shifted_index]
        result_index = (ord(substituted_char) - ord('A') - offset) % 26
        return result_index