# ... (previous code remains unchanged)

def apply_permutation(index, permutation, offset):
    shifted_index = (index + offset) % 26
    letter = permutation[shifted_index]
    new_index = (ord(letter) - ord('A') - offset) % 26
    return new_index