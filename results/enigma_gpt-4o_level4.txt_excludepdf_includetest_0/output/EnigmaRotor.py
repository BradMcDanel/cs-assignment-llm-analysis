class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._inverse_permutation = self.invert_permutation(permutation)
        self._offset = 0

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

    def apply_permutation(self, index):
        shifted_index = (index + self._offset) % 26
        permuted_char = self._permutation[shifted_index]
        permuted_index = (ord(permuted_char) - ord('A') - self._offset) % 26
        return permuted_index

    def apply_reverse_permutation(self, index):
        shifted_index = (index + self._offset) % 26
        permuted_char = self._inverse_permutation[shifted_index]
        permuted_index = (ord(permuted_char) - ord('A') - self._offset) % 26
        return permuted_index

    def invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            inverse[ord(char) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)