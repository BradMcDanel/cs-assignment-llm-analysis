import csv
import sys

# Read the CSV file into memory
def read_csv_file(file):
    data = {}
    with open(file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            name = row['name']
            data[name] = {key: int(value) for key, value in row.items() if key != 'name'}
    return data

# Read the DNA sequence file into memory
def read_dna_sequence(file):
    with open(file, 'r') as dnafile:
        return dnafile.read()

# Compute the longest run of consecutive repeats of each STR in the DNA sequence
def compute_str_counts(dna_sequence, str_counts):
    str_matches = {name: 0 for name in str_counts.keys()}

    for str_name, str_count in str_counts.items():
        longest_run = 0
        current_run = 0
        str_len = len(str_name)

        for i in range(len(dna_sequence) - str_len):
            if dna_sequence[i:i+str_len] == str_name:
                current_run += 1
            else:
                current_run = 0

            if current_run > longest_run:
                longest_run = current_run

        str_matches[str_name] = longest_run

    return str_matches

# Main program logic
def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_file = sys.argv[1]
    dna_file = sys.argv[2]

    str_counts = read_csv_file(csv_file)
    dna_sequence = read_dna_sequence(dna_file)

    str_matches = compute_str_counts(dna_sequence, str_counts)

    for name, counts in str_counts.items():
        if counts == str_matches:
            print(name)
            sys.exit(0)

    print("No match")

if __name__ == "__main__":
    main()