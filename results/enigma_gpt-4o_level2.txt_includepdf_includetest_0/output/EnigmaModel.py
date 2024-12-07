def key_pressed(self, letter):
    self._key_state[letter] = True

    # Advance the fast rotor
    carry = self._rotors[2].advance()
    if carry:
        carry = self._rotors[1].advance()
        if carry:
            self._rotors[0].advance()

    # Rest of the encryption path as before

    self.update()