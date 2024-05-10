import csv
import sys

def find_match(csv_file, dna_file):
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        str_counts = next(csv_reader)
    
    with open(dna_file, 'r') as dna_file:
        dna_sequence = dna_file.read()

    match_found = False
    for name, str_values in str_counts.items():
        if all(str(dna_sequence.count(str_value) == int(count) for str_value, count in str_values.items())):
            print(name)
            match_found = True
            break

    if not match_found:
        print("No match")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python profile.py data.csv sequence.txt")
    
    csv_file = sys.argv[1]
    dna_file = sys.argv[2]

    find_match(csv_file, dna_file)