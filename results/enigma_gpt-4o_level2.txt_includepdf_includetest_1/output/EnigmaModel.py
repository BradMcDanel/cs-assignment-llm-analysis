class EnigmaModel:
    ...
    def key_pressed(self, letter):
        # Advance the rotors
        carry = self._rotors[2].advance()
        if carry:
            carry = self._rotors[1].advance()
            if carry:
                self._rotors[0].advance()

        # Encryption process
        self._key_states[letter] = True
        index = ALPHABET.index(letter)
        index = full_encryption_path(index, self)
        translated_letter = ALPHABET[index]
        self._key_states[translated_letter] = True
        self.update()