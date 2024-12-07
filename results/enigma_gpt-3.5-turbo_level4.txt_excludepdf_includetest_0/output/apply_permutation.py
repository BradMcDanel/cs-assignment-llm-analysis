def apply_permutation(index, permutation, offset):
    shift_index = (index + offset) % 26
    new_char = permutation[shift_index]
    new_index = (ord(new_char) - ord('A') - offset) % 26
    return new_index