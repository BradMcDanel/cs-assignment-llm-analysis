import csv
import sys

def find_matching_individual(csv_file, dna_sequence_file):
    # Read the CSV file into memory
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        headers = next(csv_reader)
        individuals = list(csv_reader)

    # Read the DNA sequence file into memory
    with open(dna_sequence_file, 'r') as file:
        dna_sequence = file.read()

    # Compute the longest run of consecutive repeats of each STR in the DNA sequence
    str_counts = {}
    for header in headers.keys():
        if header != 'name':
            str_counts[header] = compute_longest_run(dna_sequence, headers[header])

    # Check for a matching individual
    for individual in individuals:
        match = True
        for header in headers.keys():
            if header != 'name':
                if int(individual[header]) != str_counts[header]:
                    match = False
                    break
        if match:
            return individual['name']

    return "No match"

def compute_longest_run(dna_sequence, str_sequence):
    longest_run = 0
    current_run = 0
    str_len = len(str_sequence)
    i = 0

    while i < len(dna_sequence):
        if dna_sequence[i:i+str_len] == str_sequence:
            current_run += 1
            i += str_len
        else:
            longest_run = max(longest_run, current_run)
            current_run = 0
            i += 1

    longest_run = max(longest_run, current_run)
    return longest_run

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_file = sys.argv[1]
    dna_sequence_file = sys.argv[2]
    
    result = find_matching_individual(csv_file, dna_sequence_file)
    print(result)