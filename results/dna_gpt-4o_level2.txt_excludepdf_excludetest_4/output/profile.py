import csv
import sys

def load_csv(filename):
    """Load the CSV file and return headers and data."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        data = list(reader)
    return headers, data

def load_dna_sequence(filename):
    """Load the DNA sequence from the text file."""
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    """Compute the longest run of subsequence in sequence."""
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

def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    csv_filename = sys.argv[1]
    headers, database = load_csv(csv_filename)

    # Read DNA sequence file into a variable
    sequence_filename = sys.argv[2]
    dna_sequence = load_dna_sequence(sequence_filename)

    # Compute longest match of each STR in DNA sequence
    str_counts = {}
    for str_seq in headers[1:]:  # Skip the first header ("name")
        str_counts[str_seq] = longest_match(dna_sequence, str_seq)

    # Check database for matching profiles
    for person in database:
        if all(str_counts[str_seq] == int(person[str_seq]) for str_seq in str_counts):
            print(person['name'])
            return

    print("No match")

if __name__ == "__main__":
    main()