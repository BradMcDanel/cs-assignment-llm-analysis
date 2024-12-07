def apply_permutation(index, permutation, offset):
    adjusted_index = (index + offset) % 26
    translated_char = permutation[adjusted_index]
    translated_index = ord(translated_char) - 65
    return (translated_index - offset) % 26

### EnigmaModel.py ###

def key_pressed(self, letter):
    self._key_state[letter] = True
    letter_index = ord(letter) - 65
    encrypted_index = apply_permutation(letter_index, self._rotors[0].get_permutation(), self._rotors[0].get_offset())
    encrypted_letter = chr(65 + encrypted_index)
    self.update()

def is_lamp_on(self, letter):
    return letter == encrypted_letter  # Lamps light up according to the encrypted letter