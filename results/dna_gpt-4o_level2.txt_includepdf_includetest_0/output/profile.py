import csv
import sys

def read_csv(filename):
    """Reads a CSV file and returns the header and data."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames
        data = list(reader)
    return header, data

def read_dna_sequence(filename):
    """Reads a text file and returns the DNA sequence."""
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    """Returns the length of the longest run of subsequence in sequence."""
    max_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while sequence[i + count*sub_len: i + (count + 1)*sub_len] == subsequence:
            count += 1
        max_run = max(max_run, count)
    
    return max_run

def main():
    # Ensure correct usage
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    # Read the DNA database and sequence
    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]
    
    header, data = read_csv(csv_filename)
    sequence = read_dna_sequence(sequence_filename)
    
    # Extract STRs from the header
    str_sequences = header[1:]  # Skip the 'name' column

    # Find longest matches for each STR
    str_counts = {str_seq: longest_match(sequence, str_seq) for str_seq in str_sequences}

    # Check database for matching profiles
    for person in data:
        if all(str_counts[str_seq] == int(person[str_seq]) for str_seq in str_sequences):
            print(person['name'])
            return
    
    print("No match")

if __name__ == "__main__":
    main()