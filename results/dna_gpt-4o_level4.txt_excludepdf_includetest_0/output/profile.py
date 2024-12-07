import csv
import sys

def read_csv_file(filename):
    """Read the CSV file and return the header and data."""
    with open(filename) as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)
    return header, data

def read_dna_sequence(filename):
    """Read the DNA sequence from a text file."""
    with open(filename) as file:
        sequence = file.read().strip()
    return sequence

def longest_consecutive_repeats(sequence, subsequence):
    """Calculate the longest run of consecutive repeats of the subsequence in the sequence."""
    max_repeats = 0
    subseq_len = len(subsequence)
    
    for i in range(len(sequence)):
        count = 0
        while sequence[i:i + subseq_len] == subsequence:
            count += 1
            i += subseq_len
        max_repeats = max(max_repeats, count)
    
    return max_repeats

def find_matching_individual(header, data, str_counts):
    """Find an individual in the data whose STR counts match the provided ones."""
    for row in data:
        name = row[0]
        counts = list(map(int, row[1:]))
        if counts == str_counts:
            return name
    return "No match"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python profile.py data.csv sequence.txt")
    
    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]
    
    # Read the CSV file and DNA sequence
    header, data = read_csv_file(csv_filename)
    dna_sequence = read_dna_sequence(sequence_filename)
    
    # Compute the longest run of consecutive repeats for each STR
    str_counts = []
    for str_seq in header[1:]:  # Skip the first column ("name")
        count = longest_consecutive_repeats(dna_sequence, str_seq)
        str_counts.append(count)
    
    # Find and print the matching individual
    print(find_matching_individual(header, data, str_counts))