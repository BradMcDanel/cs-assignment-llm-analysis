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
        if self.offset == 0:
            return True  # Carry to the next rotor
        return False

    def invert_permutation(self):
        inverted = ""
        for i in range(26):
            inverted += self.permutation[self.permutation.index(chr(65 + i))]
        return inverted