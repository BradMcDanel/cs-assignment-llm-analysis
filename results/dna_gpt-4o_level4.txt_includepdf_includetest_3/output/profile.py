import csv
import sys

def load_database(filename):
    """Load the DNA database from a CSV file."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        database = [row for row in reader]
    return database

def load_dna_sequence(filename):
    """Load the DNA sequence from a text file."""
    with open(filename, 'r') as file:
        dna_sequence = file.read().strip()
    return dna_sequence

def longest_match(sequence, subsequence):
    """Compute the longest run of consecutive repeats of the subsequence in the sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)
    
    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run

def find_match(database, str_counts, str_sequences):
    """Find and return the name of the individual whose STR counts match."""
    for person in database:
        if all(int(person[str_sequence]) == str_counts[str_sequence] for str_sequence in str_sequences):
            return person['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)
    
    database_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    database = load_database(database_filename)
    dna_sequence = load_dna_sequence(sequence_filename)

    str_sequences = list(database[0].keys())[1:]
    str_counts = {str_sequence: longest_match(dna_sequence, str_sequence) for str_sequence in str_sequences}

    match = find_match(database, str_counts, str_sequences)
    print(match)

if __name__ == "__main__":
    main()