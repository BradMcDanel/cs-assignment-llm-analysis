# File: test_enigma.py

import pytest
from EnigmaModel import EnigmaModel
from EnigmaConstants import ALPHABET, N_ROTORS

def test_enigma_initialization():
    model = EnigmaModel()
    assert len(model._rotors) == N_ROTORS
    assert all(model.get_rotor_letter(i) == 'A' for i in range(N_ROTORS))

def test_key_press_and_release():
    model = EnigmaModel()
    model.key_pressed('A')
    assert model.is_key_down('A') == True
    assert sum(model.is_lamp_on(letter) for letter in ALPHABET) == 1
    model.key_released('A')
    assert model.is_key_down('A') == False
    assert sum(model.is_lamp_on(letter) for letter in ALPHABET) == 0

def test_rotor_advance():
    model = EnigmaModel()
    initial_state = [model.get_rotor_letter(i) for i in range(N_ROTORS)]
    model.key_pressed('A')
    model.key_released('A')
    new_state = [model.get_rotor_letter(i) for i in range(N_ROTORS)]
    assert new_state != initial_state
    assert new_state[2] == ALPHABET[(ALPHABET.index(initial_state[2]) + 1) % 26]

def test_rotor_click():
    model = EnigmaModel()
    for i in range(N_ROTORS):
        initial_letter = model.get_rotor_letter(i)
        model.rotor_clicked(i)
        new_letter = model.get_rotor_letter(i)
        assert new_letter == ALPHABET[(ALPHABET.index(initial_letter) + 1) % 26]

def test_enigma_encryption():
    model = EnigmaModel()
    plaintext = "HELLO"
    ciphertext = ""
    for char in plaintext:
        model.key_pressed(char)
        ciphertext += next(letter for letter in ALPHABET if model.is_lamp_on(letter))
        model.key_released(char)
    assert ciphertext != plaintext
    assert len(ciphertext) == len(plaintext)

def test_enigma_decryption():
    model = EnigmaModel()
    plaintext = "HELLO"
    ciphertext = ""
    for char in plaintext:
        model.key_pressed(char)
        ciphertext += next(letter for letter in ALPHABET if model.is_lamp_on(letter))
        model.key_released(char)
    
    # Reset rotor positions
    for i in range(N_ROTORS):
        while model.get_rotor_letter(i) != 'A':
            model.rotor_clicked(i)
    
    decrypted = ""
    for char in ciphertext:
        model.key_pressed(char)
        decrypted += next(letter for letter in ALPHABET if model.is_lamp_on(letter))
        model.key_released(char)
    
    assert decrypted == plaintext

def test_rotor_full_rotation():
    model = EnigmaModel()
    initial_state = [model.get_rotor_letter(i) for i in range(N_ROTORS)]
    for _ in range(26):
        model.key_pressed('A')
        model.key_released('A')
    final_state = [model.get_rotor_letter(i) for i in range(N_ROTORS)]
    assert final_state[2] == initial_state[2]  # Fast rotor back to initial
    assert final_state[1] != initial_state[1]  # Middle rotor should have moved

def test_reflector():
    model = EnigmaModel()
    results = {}
    for char in ALPHABET:
        model.key_pressed(char)
        result = next(letter for letter in ALPHABET if model.is_lamp_on(letter))
        model.key_released(char)
        results[char] = result
    
    # Check that we have 13 pairs of letters
    assert len(set(results.values())) == 13
    
    # Check that no letter encrypts to itself
    for char, result in results.items():
        assert char != result

    # Reset rotors
    for i in range(N_ROTORS):
        while model.get_rotor_letter(i) != 'A':
            model.rotor_clicked(i)
    
    # Check consistency of encryption
    for char, expected_result in results.items():
        model.key_pressed(char)
        actual_result = next(letter for letter in ALPHABET if model.is_lamp_on(letter))
        model.key_released(char)
        assert actual_result == expected_result, f"Inconsistent encryption for {char}"

    # Print the reflector mapping for debugging
    print("Reflector mapping:")
    for char, result in sorted(results.items()):
        print(f"{char} -> {result}")

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])
