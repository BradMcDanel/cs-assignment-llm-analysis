import csv
import sys

def read_csv_file(csv_filename):
    """Reads the CSV file and returns a list of dictionaries, each representing an individual."""
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def read_dna_sequence(txt_filename):
    """Reads the DNA sequence from a text file and returns it as a string."""
    with open(txt_filename, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    """Returns the longest run of consecutive repeats of `subsequence` in `sequence`."""
    longest_run = 0
    subseq_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while sequence[i:i + subseq_len] == subsequence:
            count += 1
            i += subseq_len

        longest_run = max(longest_run, count)

    return longest_run

def find_dna_match(database, sequence):
    """Finds the individual whose STR counts match the sequence's STR counts."""
    # Extract STRs from the first individual (assuming all have the same STRs in the same order)
    str_names = database[0].keys() - {'name'}

    # Calculate longest match for each STR
    str_counts = {str_name: longest_match(sequence, str_name) for str_name in str_names}

    # Compare against each individual in the database
    for person in database:
        if all(int(person[str_name]) == str_counts[str_name] for str_name in str_names):
            return person['name']

    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_filename = sys.argv[1]
    txt_filename = sys.argv[2]

    # Read the database and DNA sequence
    database = read_csv_file(csv_filename)
    dna_sequence = read_dna_sequence(txt_filename)

    # Find and print the DNA match
    match = find_dna_match(database, dna_sequence)
    print(match)

if __name__ == "__main__":
    main()