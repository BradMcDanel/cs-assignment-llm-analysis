def apply_permutation(index, permutation, offset):
    # Shift the index by the offset
    shifted_index = (index + offset) % 26
    # Apply the permutation
    permuted_char = permutation[shifted_index]
    # Shift back and return the new index
    return (ord(permuted_char) - 65 - offset) % 26

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

    def apply_forward(self, index):
        return apply_permutation(index, self._permutation, self._offset)

    def apply_backward(self, index):
        return apply_permutation(index, self._inverse_permutation, self._offset)

    # ... (other methods remain the same)