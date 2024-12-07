import csv
import sys

def read_dna_database(filename):
    """Read the DNA database CSV file and return a list of individuals with their STR counts."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def read_dna_sequence(filename):
    """Read the DNA sequence from a text file and return it as a string."""
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    """Returns the length of the longest run of subsequence in the sequence."""
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while sequence[i:i + sub_len] == subsequence:
            count += 1
            i += sub_len
        longest_run = max(longest_run, count)

    return longest_run

def find_matching_individual(database, str_counts):
    """Find the individual whose STR counts match the computed STR counts."""
    for person in database:
        if all(int(person[str_name]) == str_counts[str_name] for str_name in str_counts):
            return person['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read the CSV file and DNA sequence file
    database = read_dna_database(sys.argv[1])
    dna_sequence = read_dna_sequence(sys.argv[2])

    # Extract STRs from the database header
    str_names = database[0].keys() - {'name'}

    # Compute longest match for each STR
    str_counts = {str_name: longest_match(dna_sequence, str_name) for str_name in str_names}

    # Find and print the matching individual
    match = find_matching_individual(database, str_counts)
    print(match)

if __name__ == "__main__":
    main()