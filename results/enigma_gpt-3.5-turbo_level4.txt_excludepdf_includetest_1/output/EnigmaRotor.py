class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.offset = 0

    def get_offset(self):
        return self.offset

    def get_permutation(self):
        return self.permutation

    def advance(self):
        self.offset = (self.offset + 1) % 26

def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    new_letter = permutation[shifted_index]
    new_index = (ord(new_letter) - ord('A') - offset) % 26
    return chr(new_index + ord('A'))