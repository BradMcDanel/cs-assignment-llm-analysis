import csv
import sys

def find_match(csv_file, dna_file):
    # Read the CSV file into memory
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    # Read the DNA sequence file into memory
    with open(dna_file, 'r') as dnafile:
        dna_sequence = dnafile.read()

    # Extract the STR sequences from the first row of the CSV file
    str_sequences = list(rows[0].keys())[1:]

    # Compute the longest run of consecutive repeats for each STR in the DNA sequence
    longest_runs = {}
    for sequence in str_sequences:
        longest_run = 0
        current_run = 0
        sequence_length = len(sequence)
        for i in range(len(dna_sequence)):
            if dna_sequence[i:i+sequence_length] == sequence:
                current_run += 1
                if current_run > longest_run:
                    longest_run = current_run
            else:
                current_run = 0
        longest_runs[sequence] = longest_run

    # Check if any individual in the CSV file matches the longest runs of STRs in the DNA sequence
    for row in rows:
        if all(int(row[sequence]) == longest_runs[sequence] for sequence in str_sequences):
            print(row['name'])
            return

    print("No match")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
    else:
        find_match(sys.argv[1], sys.argv[2])