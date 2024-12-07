import subprocess
import re

def print_subject_1694(police_shootings_output):
    print(re.search(r"Philando Castile", police_shootings_output, re.IGNORECASE))

def print_minnesota_subjects(police_shootings_output):
    expected_names = ["Marcus Golden", "Quincy Reed Reindl", "Raymond Kmetz", ...]  # Truncated for brevity
    for name in expected_names:
        print(re.search(re.escape(name), police_shootings_output, re.IGNORECASE))

def print_black_fraction_output(police_shootings_output):
    print(re.search(r"0\.23[2-3]|0\.23", police_shootings_output))

def print_unarmed_black_fraction_output(police_shootings_output):
    print(re.search(r"0\.31[89]|0\.32", police_shootings_output))

if __name__ == "__main__":
    output = subprocess.check_output(["python", "police_shootings.py"], universal_newlines=True)
    print_subject_1694(output)
    print_minnesota_subjects(output)
    print_black_fraction_output(output)
    print_unarmed_black_fraction_output(output)