import pytest
import subprocess
import os
import re

def run_main_py(input_file):
    possible_names = ["Assignment4.py", "assignment4.py", "main.py", "Main.py"]
    script_name = None
    for name in possible_names:
        if os.path.isfile(name):
            script_name = name
            break
    if script_name is None:
        raise FileNotFoundError("Neither Assignment4.py nor main.py was found in any case variation.")

    return subprocess.check_output(["python", script_name, input_file], universal_newlines=True)

def read_output_file(output_file):
    with open(output_file, "r") as file:
        return file.read().strip()

def normalize_string(s):
    return re.sub(r'\s+', ' ', s.lower().strip())

def compare_predator_prey_lines(actual, expected):
    actual_dict = {}
    expected_dict = {}
    
    for line in actual:
        parts = line.split(' eats ')
        if len(parts) == 2:
            predator, prey = parts
            actual_dict[normalize_string(predator)] = set(normalize_string(prey).replace(' and ', ', ').split(', '))
    
    for line in expected:
        parts = line.split(' eats ')
        if len(parts) == 2:
            predator, prey = parts
            expected_dict[normalize_string(predator)] = set(normalize_string(prey).replace(' and ', ', ').split(', '))
    
    return actual_dict == expected_dict

def compare_lists(actual, expected, ignore_order=True, is_predator_prey=False):
    if is_predator_prey:
        return compare_predator_prey_lines(actual, expected)
    
    actual = [normalize_string(item) for item in actual]
    expected = [normalize_string(item) for item in expected]
    if ignore_order:
        return set(actual) == set(expected)
    return actual == expected

def extract_section(output, section_name):
    pattern = rf"{section_name}:?([\s\S]*?)(?:\n\n|\Z)"
    match = re.search(pattern, output, re.IGNORECASE)
    if match:
        return [line.strip() for line in match.group(1).strip().split('\n') if line.strip()]
    return []

@pytest.fixture(params=[
    ("AnotherFoodWeb.txt", "AnotherFoodWeb_Output.txt"),
    ("AquaticFoodWeb.txt", "AquaticFoodWeb_Output.txt"),
    ("GrasslandFoodWeb.txt", "GrasslandFoodWeb_Output.txt"),
    ("MixedFoodWeb.txt", "MixedFoodWeb_Output.txt"),
    ("SimpleFoodWeb.txt", "SimpleFoodWeb_Output.txt"),
    ("TerrestrialFoodWeb.txt", "TerrestrialFoodWeb_Output.txt")
])
def food_web_files(request):
    return request.param

@pytest.fixture
def main_output(food_web_files):
    input_file, _ = food_web_files
    return run_main_py(input_file)

@pytest.fixture
def expected_output(food_web_files):
    _, output_file = food_web_files
    return read_output_file(output_file)

def test_predators_and_prey(main_output, expected_output):
    main_predators = extract_section(main_output, "Predators and Prey")
    expected_predators = extract_section(expected_output, "Predators and Prey")
    
    assert compare_lists(main_predators, expected_predators, is_predator_prey=True), \
        f"Predators and Prey mismatch. \nExpected: {expected_predators}\nGot: {main_predators}"

# ... (rest of the test functions remain the same)
