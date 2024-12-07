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

    def apply_permutation(self, index, right_to_left=True):
        if right_to_left:
            return self.apply_permutation_static(index, self.permutation, self.offset)
        else:
            return self.apply_permutation_static(index, self.inverse_permutation, self.offset)

    @staticmethod
    def apply_permutation_static(index, permutation, offset):
        shifted_index = (index + offset) % 26
        letter = permutation[shifted_index]
        new_index = (ord(letter) - 65 - offset) % 26
        return new_index

    @staticmethod
    def invert_permutation(permutation):
        inverse = [''] * 26
        for i, char in enumerate(permutation):
            inverse[ord(char) - 65] = chr(i + 65)
        return ''.join(inverse)