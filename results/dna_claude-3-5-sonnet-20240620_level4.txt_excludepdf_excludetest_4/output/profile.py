import csv
import sys

def read_csv(filename):
    """Read the CSV file and return a dictionary of individuals and their STR counts."""
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return {row['name']: {key: int(value) for key, value in row.items() if key != 'name'} for row in reader}

def read_dna_sequence(filename):
    """Read the DNA sequence from a file."""
    with open(filename, 'r') as file:
        return file.read().strip()

def compute_longest_run(sequence, str_sequence):
    """Compute the longest run of consecutive repeats of the STR in the DNA sequence."""
    longest_run = 0
    length = len(str_sequence)
    for i in range(len(sequence)):
        current_run = 0
        while sequence[i:i+length] == str_sequence:
            current_run += 1
            i += length
        longest_run = max(longest_run, current_run)
    return longest_run

def find_match(database, sequence):
    """Find a match in the database for the given DNA sequence."""
    str_counts = {str_name: compute_longest_run(sequence, str_name) for str_name in database[next(iter(database))].keys()}
    
    for name, counts in database.items():
        if all(counts[str_name] == str_counts[str_name] for str_name in counts):
            return name
    
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    database = read_csv(database_file)
    sequence = read_dna_sequence(sequence_file)

    match = find_match(database, sequence)
    print(match)

if __name__ == "__main__":
    main()