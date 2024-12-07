import csv
import sys

def read_csv_file(filename):
    """Reads the CSV file and returns the data as a list of dictionaries."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def read_dna_sequence(filename):
    """Reads the DNA sequence from a text file and returns it as a string."""
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    """Computes the longest run of consecutive repeats of a subsequence in a sequence."""
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)
    
    for i in range(seq_len):
        count = 0
        while sequence[i + count * sub_len: i + (count + 1) * sub_len] == subsequence:
            count += 1
        longest_run = max(longest_run, count)
        
    return longest_run

def find_matching_individual(dna_database, str_counts, str_sequences):
    """Finds the matching individual from the DNA database given STR counts."""
    for person in dna_database:
        if all(int(person[str_seq]) == str_counts[str_seq] for str_seq in str_sequences):
            return person['name']
    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    # Read CSV file
    dna_database = read_csv_file(csv_filename)
    str_sequences = dna_database[0].keys() - {'name'}

    # Read DNA sequence
    dna_sequence = read_dna_sequence(dna_filename)

    # Calculate STR counts from the DNA sequence
    str_counts = {str_seq: longest_match(dna_sequence, str_seq) for str_seq in str_sequences}

    # Find the matching individual
    match = find_matching_individual(dna_database, str_counts, str_sequences)
    print(match)