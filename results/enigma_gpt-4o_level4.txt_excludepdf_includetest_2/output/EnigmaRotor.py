class EnigmaRotor:

    def __init__(self, permutation):
        self.permutation = permutation
        self.inverse_permutation = self.invert_permutation(permutation)
        self.offset = 0

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26
        return self.offset == 0

    def apply_permutation(self, index):
        shifted_index = (index + self.offset) % 26
        char = self.permutation[shifted_index]
        return (ord(char) - ord('A') - self.offset) % 26

    def apply_inverse_permutation(self, index):
        shifted_index = (index + self.offset) % 26
        char = self.inverse_permutation[shifted_index]
        return (ord(char) - ord('A') - self.offset) % 26

    def invert_permutation(self, permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            inverse[ord(char) - ord('A')] = chr(i + ord('A'))
        return ''.join(inverse)