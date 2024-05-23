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
    expected_names = [
        "Marcus Golden", "Quincy Reed Reindl", "Raymond Kmetz", "Justin Tolkinen",
        "Sam Holmes", "Derek Wolfsteller", "Adam Schneider", "Philip Quinn",
        "Robert Christen", "Luverne Roy Christensen", "Jamar Clark", "Michael Kirvelay",
        "John Birkeland", "Map Kong", "Denise Fairchild", "Raul Salvador Marquez Heraldes",
        "Jaffort Smith", "Eugene Geno Francis Smith", "Philando Castile", "Adam Jo Klimek",
        "Justin Kulhanek-Derks", "Dahir Adan", "Jamie Joseph Lewis", "Kristofer Daniel Youngquist",
        "Jay Johannes Holmgren", "Chase Anthony Tuseth", "Ronnie Johnson", "Jamison Christopher Anderson",
        "Cordale Quinn Handy", "Clarence Duane Huderle", "Darren Jahnke", "Gregory Shawn Thrower",
        "Justine Damond", "Phumee Lee", "Ronald L. Klitzka", "Jeffrey John Golnick",
        "Nicholas Daniel Moore", "Gilbert Salas", "Benjamin Evans", "Thurman Blevins",
        "Archer Amorosi", "William James Hughes", "Keagan Johnson", "Travis Jordan",
        "James Hanchett", "Keaton James Larson", "J Scot Alan Widmark", "Vernon May",
        "Joseph Roberts", "Matthew Neil Tuhkanen", "Tyler Schmidtbauer", "John Duane Fairbanks",
        "Timothy Russell Majchrzak", "Isak Abdirahman Aden", "Mario Benjamin", "Kobe Heisler",
        "Brian Quinones", "Ronald Davis", "Chiasher Fong Vue", "Kent Richard Kruger",
        "Keith P. Haux", "Austin Dean Heights", "Arlan Kaleb Schultz", "Kirby Joseph Michael Hengel",
        "Anthony Michael Legato", "Estavon Elioff", "Dolal Idd", "Brian Andren",
        "Dominic Lucas Koch", "David Joseph Wayne Conwell", "Shannon Savela", "David Savela",
        "Daunte Wright", "Bradley Michael Olsen", "Winston Boogie Smith Jr.", "Ricardo Torres Jr.",
        "Noah Douglas Kelly", "Bradley George Erickson", "Kokou Christopher Fiafonou", "Amir Locke",
        "Jesse Henri Werling", "Michael David Johnson", "Charles Bangs", "Andrew Tekle Sundberg",
        "Joshua Hippler", "Jordyn John Hansen", "Howard Johnson", "Brent A. Alsleben"
    ]
    for name in expected_names:
        assert re.search(re.escape(name), police_shootings_output, re.IGNORECASE)

def test_black_fraction_output(police_shootings_output):
    assert re.search(r"0\.232", police_shootings_output)

def test_unarmed_black_fraction_output(police_shootings_output):
    assert re.search(r"0\.319", police_shootings_output)
