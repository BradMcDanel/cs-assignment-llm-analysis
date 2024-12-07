import csv
import sys

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        # Check for a subsequence match in a "window" within the sequence
        count = 0
        while (i + count * sub_len) < seq_len and sequence[i + count * sub_len : i + (count + 1) * sub_len] == subsequence:
            count += 1
        # Update longest run found
        longest_run = max(longest_run, count)
    
    return longest_run

def read_csv_file(filename):
    """Reads a CSV file and returns the header and a list of dictionaries for each row."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data

def read_dna_sequence(filename):
    """Reads a DNA sequence from a text file."""
    with open(filename, 'r') as file:
        sequence = file.read().strip()
    return sequence

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    # Read the CSV file and DNA sequence file
    database = read_csv_file(sys.argv[1])
    dna_sequence = read_dna_sequence(sys.argv[2])

    # Get the list of STRs from the first row of the CSV file
    str_keys = list(database[0].keys())[1:]  # Skip the 'name' field

    # Compute longest match for each STR in the DNA sequence
    str_counts = {str_key: longest_match(dna_sequence, str_key) for str_key in str_keys}

    # Check each individual in the database for matching STR counts
    for person in database:
        if all(int(person[str_key]) == str_counts[str_key] for str_key in str_keys):
            print(person['name'])
            return
    
    print("No match")

if __name__ == "__main__":
    main()