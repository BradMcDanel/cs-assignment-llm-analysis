import csv
import sys

def read_csv(file_path):
    """Reads the CSV file and returns the fieldnames and data."""
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames  # Get STR names
        data = [row for row in reader]  # Read data
    return fieldnames, data

def read_dna_sequence(file_path):
    """Reads the DNA sequence from a text file."""
    with open(file_path, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_str_run(sequence, str_sequence):
    """Calculates the longest run of consecutive repeats of the STR in the DNA sequence."""
    max_run = 0
    str_len = len(str_sequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        # Initialize count for this position
        count = 0

        # Check for consecutive repeats
        while sequence[i:i + str_len] == str_sequence:
            count += 1
            i += str_len

        # Update max_run if this run is the longest
        max_run = max(max_run, count)

    return max_run

def find_matching_individual(fieldnames, data, dna_sequence):
    """Finds the matching individual from database based on DNA sequence."""
    str_names = fieldnames[1:]  # Exclude 'name' from STR names
    str_counts = {str_name: longest_str_run(dna_sequence, str_name) for str_name in str_names}

    for person in data:
        if all(int(person[str_name]) == str_counts[str_name] for str_name in str_names):
            return person['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_file_path = sys.argv[1]
    dna_file_path = sys.argv[2]

    # Read the CSV and DNA sequence
    fieldnames, data = read_csv(csv_file_path)
    dna_sequence = read_dna_sequence(dna_file_path)

    # Find and print the matching individual
    result = find_matching_individual(fieldnames, data, dna_sequence)
    print(result)

if __name__ == "__main__":
    main()