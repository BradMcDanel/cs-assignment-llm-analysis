import csv
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read CSV file into memory
    csv_filename = sys.argv[1]
    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            dna_data = {key: int(value) for key, value in row.items() if key != 'name'}

    # Read DNA sequence file into memory
    sequence_filename = sys.argv[2]
    with open(sequence_filename, 'r') as seq_file:
        dna_sequence = seq_file.read()

    # Compute the longest run of consecutive repeats of each STR in the DNA sequence
    longest_runs = {}
    for key in dna_data.keys():
        longest_runs[key] = compute_longest_run(dna_sequence, key)

    # Match the longest runs with individuals in the CSV file
    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            name = row['name']
            if all(int(row[key]) == longest_runs[key] for key in longest_runs.keys()):
                print(name)
                return

    print("No match")

def compute_longest_run(dna_sequence, str_sequence):
    max_repeats = 0
    current_repeats = 0
    str_len = len(str_sequence)

    for i in range(len(dna_sequence) - str_len):
        if dna_sequence[i:i + str_len] == str_sequence:
            current_repeats += 1
            max_repeats = max(max_repeats, current_repeats)
        else:
            current_repeats = 0

    return max_repeats

if __name__ == "__main__":
    main()