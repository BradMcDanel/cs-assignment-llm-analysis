import csv
import sys

def compute_longest_run(dna_sequence, str_sequence):
    longest_run = 0
    current_run = 0

    for i in range(len(dna_sequence)):
        if dna_sequence[i:i+len(str_sequence)] == str_sequence:
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            current_run = 0

    return longest_run

def identify_dna_owner(csv_file, sequence_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        headers = next(csv_reader)
        data = {row['name']: [int(row[header]) for header in headers if header != 'name'] for row in csv_reader}

    with open(sequence_file, 'r') as file:
        dna_sequence = file.read()

    for name, str_counts in data.items():
        match = True
        for i, str_count in enumerate(str_counts):
            str_sequence = headers[i+1]
            longest_run = compute_longest_run(dna_sequence, str_sequence)
            if longest_run != str_count:
                match = False
                break
        if match:
            print(name)
            return

    print("No match")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
    else:
        identify_dna_owner(sys.argv[1], sys.argv[2])