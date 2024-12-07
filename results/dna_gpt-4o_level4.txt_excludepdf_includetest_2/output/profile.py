import csv
import sys

def read_csv(filename):
    # Open and read the CSV file containing STR counts
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        str_list = reader.fieldnames[1:]  # Get the list of STRs
        database = list(reader)  # Read the entire CSV into a list of dictionaries
    return str_list, database

def read_dna_sequence(filename):
    # Open and read the DNA sequence file
    with open(filename, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    # Compute the longest run of a subsequence in the DNA sequence
    max_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        # Initialize count for a new potential run
        count = 0

        # Check for repeat occurrences of the subsequence starting from position i
        while sequence[i:i + sub_len] == subsequence:
            count += 1
            i += sub_len

        # Update max_run if this run is longer
        max_run = max(max_run, count)

    return max_run

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    # Read data from CSV and DNA sequence files
    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    str_list, database = read_csv(csv_filename)
    dna_sequence = read_dna_sequence(sequence_filename)

    # Compute the longest match of each STR in the DNA sequence
    str_counts = {str_: longest_match(dna_sequence, str_) for str_ in str_list}

    # Compare the STR counts with each individual's STR counts in the database
    for person in database:
        if all(str_counts[str_] == int(person[str_]) for str_ in str_list):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()