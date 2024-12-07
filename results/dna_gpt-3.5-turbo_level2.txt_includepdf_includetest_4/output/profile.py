import csv
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    data_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Read the CSV file
    with open(data_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dna_data = {key: int(value) for key, value in row.items()}

    # Read the DNA sequence
    with open(sequence_file, "r") as file:
        dna_sequence = file.read()

    # Compute the longest run of consecutive repeats for each STR
    longest_runs = {}
    for key in dna_data.keys():
        longest_runs[key] = compute_longest_run(dna_sequence, key)

    # Check for a match in the DNA database
    for name, counts in dna_data.items():
        if all(counts[key] == longest_runs[key] for key in counts.keys()):
            print(name)
            return

    print("No match")

def compute_longest_run(sequence, str_key):
    longest_run = 0
    current_run = 0
    str_len = len(str_key)
    i = 0
    
    while i < len(sequence):
        if sequence[i:i+str_len] == str_key:
            current_run += 1
            i += str_len
        else:
            longest_run = max(longest_run, current_run)
            current_run = 0
            i += 1

    return longest_run

if __name__ == "__main__":
    main()