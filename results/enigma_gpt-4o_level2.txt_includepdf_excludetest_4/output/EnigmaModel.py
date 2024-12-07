# ... (previous code remains unchanged)

    def key_pressed(self, letter):
        carry = self._rotors[2].advance()
        if carry:
            carry = self._rotors[1].advance()
            if carry:
                self._rotors[0].advance()
        
        # Encryption logic remains unchanged
        index = ord(letter) - ord('A')
        index = apply_permutation(index, self._rotors[2].get_permutation(), self._rotors[2].get_offset())
        index = apply_permutation(index, self._rotors[1].get_permutation(), self._rotors[1].get_offset())
        index = apply_permutation(index, self._rotors[0].get_permutation(), self._rotors[0].get_offset())
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        index = apply_permutation(index, self._rotors[0].get_permutation(), self._rotors[0].get_offset())
        index = apply_permutation(index, self._rotors[1].get_permutation(), self._rotors[1].get_offset())
        index = apply_permutation(index, self._rotors[2].get_permutation(), self._rotors[2].get_offset())
        self._lamp_state = {chr(i + ord('A')): i == index for i in range(26)}
        self.update()

# ... (rest of the code remains unchanged)