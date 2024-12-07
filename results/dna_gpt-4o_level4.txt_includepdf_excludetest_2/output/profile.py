import csv
import sys

def read_csv(file_path):
    """Read the CSV file and return the header and data."""
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data = list(reader)
    return header, data

def read_dna_sequence(file_path):
    """Read the DNA sequence from the text file."""
    with open(file_path, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    """Find the longest run of a subsequence in a sequence."""
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while sequence[i:i+sub_len] == subsequence:
            count += 1
            i += sub_len

        longest_run = max(longest_run, count)

    return longest_run

def find_matching_individual(header, data, profile):
    """Find the individual matching the DNA profile."""
    for row in data:
        name = row[0]
        str_counts = list(map(int, row[1:]))
        if str_counts == profile:
            return name
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        sys.exit(1)

    csv_file = sys.argv[1]
    dna_file = sys.argv[2]

    header, data = read_csv(csv_file)
    sequence = read_dna_sequence(dna_file)
    strs = header[1:]

    profile = [longest_match(sequence, str_seq) for str_seq in strs]
    match = find_matching_individual(header, data, profile)
    
    print(match)

if __name__ == "__main__":
    main()