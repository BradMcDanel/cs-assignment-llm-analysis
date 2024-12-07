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
        return self.offset == 0