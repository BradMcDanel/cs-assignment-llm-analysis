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

    def invert_permutation(self, permutation):
        inverted = [''] * 26
        for i, char in enumerate(permutation):
            inverted[ord(char) - 65] = chr(i + 65)
        return ''.join(inverted)