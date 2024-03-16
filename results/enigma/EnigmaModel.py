from EnigmaConstants import ALPHABET, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION

class EnigmaRotor:
    def __init__(self, permutation):
        self.permutation = permutation
        self.offset = 0
    
    def advance(self):
        self.offset = (self.offset + 1) % len(ALPHABET)
        return self.offset == 0
    
    def get_encryption_letter(self, letter, reverse=False):
        index = ALPHABET.index(letter)
        if not reverse:
            index = (index + self.offset) % len(ALPHABET)
            encrypted_letter = self.permutation[index]
            return ALPHABET[(ALPHABET.index(encrypted_letter) - self.offset) % len(ALPHABET)]
        else:
            index = (index - self.offset + len(ALPHABET)) % len(ALPHABET)
            encrypted_letter = ALPHABET[self.permutation.index(ALPHABET[index])]
            return ALPHABET[(ALPHABET.index(encrypted_letter) + self.offset) % len(ALPHABET)]

class EnigmaModel:
    def __init__(self):
        self.rotors = [EnigmaRotor(permutation) for permutation in ROTOR_PERMUTATIONS]
        self.pressed_keys = set()
    
    def encrypt_letter(self, letter):
        for rotor in reversed(self.rotors):
            letter = rotor.get_encryption_letter(letter)
        letter = ALPHABET[REFLECTOR_PERMUTATION.index(letter)]
        for rotor in self.rotors:
            letter = rotor.get_encryption_letter(letter, reverse=True)
        return letter

    def handle_key_press(self, letter):
        self.rotors[-1].advance()
        return self.encrypt_letter(letter)

# This is a simplified demonstration that does not include the full MVC setup or the GUI.
if __name__ == "__main__":
    enigma = EnigmaModel()
    encoded_letter = enigma.handle_key_press('A')
    print(f"Encoded letter: {encoded_letter}")