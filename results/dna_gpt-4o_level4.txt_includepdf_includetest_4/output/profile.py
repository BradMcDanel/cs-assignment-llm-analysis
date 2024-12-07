import csv
import sys

def read_csv(filename):
    """Read the CSV file and return the header and data."""
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data = [row for row in reader]
    return header, data

def read_dna_sequence(filename):
    """Read the DNA sequence from a file."""
    with open(filename) as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    """Returns the length of the longest run of `subsequence` in `sequence`."""
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while sequence[i + count * sub_len: i + (count + 1) * sub_len] == subsequence:
            count += 1
        longest_run = max(longest_run, count)
    
    return longest_run

def find_match(database, str_counts, strs):
    """Find a matching profile in the database."""
    for row in database:
        name = row[0]
        counts = list(map(int, row[1:]))
        if counts == str_counts:
            return name
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    header, database = read_csv(csv_filename)
    dna_sequence = read_dna_sequence(dna_filename)
    strs = header[1:]

    str_counts = [longest_match(dna_sequence, str_seq) for str_seq in strs]
    match = find_match(database, str_counts, strs)
    print(match)

if __name__ == "__main__":
    main()