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
        return self._offset == 0  # Return True if we've made a full revolution

def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    new_char = permutation[shifted_index]
    return (ord(new_char) - ord('A') - offset) % 26