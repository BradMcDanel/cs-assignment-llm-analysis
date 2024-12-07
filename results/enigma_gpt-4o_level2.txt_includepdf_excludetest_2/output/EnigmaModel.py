def key_pressed(self, letter):
    self._key_states[letter] = True
    # Advance rotors appropriately
    carry = self._rotors[2].advance()
    if carry:
        carry = self._rotors[1].advance()
        if carry:
            self._rotors[0].advance()

    # Remaining encryption logic remains the same
    # ...

# Update advance method to return a Boolean
def advance(self):
    self.offset = (self.offset + 1) % 26
    return self.offset == 0  # Return True if it wraps around