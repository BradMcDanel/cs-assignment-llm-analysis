import pytest
import subprocess
import re

@pytest.fixture(scope="module")
def police_shootings_output():
    output = subprocess.check_output(["python", "police_shootings.py"], universal_newlines=True)
    return output

def test_subject_1694(police_shootings_output):
    assert re.search(r"Philando Castile", police_shootings_output, re.IGNORECASE)

def test_minnesota_subjects(police_shootings_output):
    expected_names = ["Marcus Golden", "Quincy Reed Reindl", ...]  # List shortened for brevity
    for name in expected_names:
        assert re.search(re.escape(name), police_shootings_output, re.IGNORECASE)

def test_black_fraction_output(police_shootings_output):
    assert re.search(r"0\.23[2-3]|0\.23", police_shootings_output)

def test_unarmed_black_fraction_output(police_shootings_output):
    assert re.search(r"0\.31[89]|0\.32", police_shootings_output)