def key_pressed(self, letter):
        self._key_states[letter] = True

        # Advance rotors
        carry = self._rotors[2].advance()
        if carry:
            carry = self._rotors[1].advance()
            if carry:
                self._rotors[0].advance()

        # Encryption logic here...

        self.update()