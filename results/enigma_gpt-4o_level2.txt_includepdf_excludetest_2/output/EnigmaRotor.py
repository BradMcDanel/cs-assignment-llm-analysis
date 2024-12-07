class EnigmaRotor:
    def __init__(self, permutation):
        self._permutation = permutation
        self._offset = 0
        self._inverse_permutation = self.invert_permutation(permutation)

    def get_offset(self):
        return self._offset

    def get_permutation(self):
        return self._permutation

    def advance(self):
        self._offset = (self._offset + 1) % 26
        return self._offset == 0

    def apply_permutation(self, index):
        shifted_index = (index + self._offset) % 26
        translated_char = self._permutation[shifted_index]
        return (ord(translated_char) - ord('A') - self._offset) % 26

    def apply_inverse_permutation(self, index):
        shifted_index = (index + self._offset) % 26
        translated_char = self._inverse_permutation[shifted_index]
        return (ord(translated_char) - ord('A') - self._offset) % 26

    @staticmethod
    def invert_permutation(permutation):
        inverse_permutation = [''] * 26
        for i, char in enumerate(permutation):
            index = ord(char) - ord('A')
            inverse_permutation[index] = chr(ord('A') + i)
        return ''.join(inverse_permutation)

# Example usage
if __name__ == "__main__":
    rotor = EnigmaRotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
    print(rotor.apply_permutation(16))  # Q -> I
    print(rotor.apply_inverse_permutation(8))  # I -> Q