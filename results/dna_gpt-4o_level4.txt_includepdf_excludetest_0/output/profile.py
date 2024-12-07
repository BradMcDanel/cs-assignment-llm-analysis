import csv
import sys

def read_csv(filename):
    """Reads the CSV file and returns the data as a list of dictionaries."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def read_dna_sequence(filename):
    """Reads the DNA sequence from a text file."""
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    """Returns the longest run of subsequence in sequence."""
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while True:
            start = i + count * sub_len
            end = start + sub_len
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)

    return longest_run

def find_dna_owner(database, dna_sequence, strs):
    """Compares the STR counts from DNA sequence with each individual in the database."""
    # Compute the longest match of each STR in the DNA sequence
    str_counts = {str_: longest_match(dna_sequence, str_) for str_ in strs}

    # Compare against each person in the database
    for person in database:
        # Check if all STR counts match
        if all(int(person[str_]) == str_counts[str_] for str_ in strs):
            return person['name']
    return "No match"

def main():
    # Check for correct command-line usage
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    # Read the database and DNA sequence files
    database_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    database = read_csv(database_filename)
    dna_sequence = read_dna_sequence(dna_filename)

    # Get the list of STRs from the database (first line of CSV, excluding 'name')
    strs = list(database[0].keys())[1:]

    # Find and print the name of the person to whom the DNA belongs
    owner = find_dna_owner(database, dna_sequence, strs)
    print(owner)

if __name__ == "__main__":
    main()