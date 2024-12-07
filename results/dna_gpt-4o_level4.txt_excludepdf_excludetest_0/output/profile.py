import csv
import sys

def read_csv(filename):
    """Read the CSV file and return the headers and rows."""
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)
    return headers, rows

def read_dna_sequence(filename):
    """Read the DNA sequence from a text file."""
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    """Return length of longest run of subsequence in sequence."""
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

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_filename = sys.argv[1]
    dna_filename = sys.argv[2]

    # Read CSV and DNA sequence
    headers, rows = read_csv(csv_filename)
    dna_sequence = read_dna_sequence(dna_filename)

    # Compute longest match for each STR
    str_counts = {}
    for str_seq in headers[1:]:  # Skip the 'name' column
        str_counts[str_seq] = longest_match(dna_sequence, str_seq)

    # Find a matching profile
    for row in rows:
        name = row[0]
        counts = list(map(int, row[1:]))
        if counts == [str_counts[header] for header in headers[1:]]:
            print(name)
            return
    
    print("No match")

if __name__ == "__main__":
    main()