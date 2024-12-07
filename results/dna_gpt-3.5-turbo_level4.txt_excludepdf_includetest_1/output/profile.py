import csv
import sys

def find_dna_match(csv_file, dna_file):
    # Read the CSV file
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        dna_database = [row for row in csv_reader]

    # Read the DNA sequence file
    with open(dna_file, mode='r') as file:
        dna_sequence = file.read()

    # Extract the STR sequences from the CSV file
    str_sequences = list(csv_reader.fieldnames[1:])

    # Find the longest consecutive repeats of each STR in the DNA sequence
    str_counts = {}
    for str_seq in str_sequences:
        longest_run = 0
        current_run = 0
        str_length = len(str_seq)
        for i in range(len(dna_sequence)):
            if dna_sequence[i:i + str_length] == str_seq:
                current_run += 1
                if current_run > longest_run:
                    longest_run = current_run
            else:
                current_run = 0
        str_counts[str_seq] = longest_run

    # Check if any individual in the DNA database matches the STR counts
    for person in dna_database:
        if all(int(person[str_seq]) == str_counts[str_seq] for str_seq in str_sequences):
            return person['name']

    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
    else:
        result = find_dna_match(sys.argv[1], sys.argv[2])
        print(result)