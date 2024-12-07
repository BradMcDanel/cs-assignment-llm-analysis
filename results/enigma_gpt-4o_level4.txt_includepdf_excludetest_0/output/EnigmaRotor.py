# File: EnigmaRotor.py

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.offset = 0
        self.inverse_permutation = self.invert_permutation(permutation)

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def apply_permutation(self, index, offset):
        shifted_index = (index + offset) % 26
        letter = self.permutation[shifted_index]
        return (ord(letter) - ord('A') - offset) % 26

    def apply_inverse_permutation(self, index, offset):
        shifted_index = (index + offset) % 26
        letter = self.inverse_permutation[shifted_index]
        return (ord(letter) - ord('A') - offset) % 26

    def invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, letter in enumerate(permutation):
            inverse[ord(letter) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)