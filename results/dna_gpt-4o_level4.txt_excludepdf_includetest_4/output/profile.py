import csv
import sys

def read_csv(filename):
    """Read the CSV file and return the header and data as lists."""
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data = [row for row in reader]
    return header, data

def read_dna_sequence(filename):
    """Read the DNA sequence from a file."""
    with open(filename, 'r') as file:
        return file.read().strip()

def longest_str_repeat(sequence, str_pattern):
    """Return the longest run of consecutive repeats of `str_pattern` in `sequence`."""
    max_count = 0
    pattern_length = len(str_pattern)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while sequence[i:i + pattern_length] == str_pattern:
            count += 1
            i += pattern_length

        max_count = max(max_count, count)

    return max_count

def find_matching_profile(header, data, str_counts):
    """Find the individual in the data that matches the given STR counts."""
    for row in data:
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
    sequence_filename = sys.argv[2]

    # Read CSV and DNA sequence
    header, data = read_csv(csv_filename)
    dna_sequence = read_dna_sequence(sequence_filename)

    # Compute longest STR repeats for each STR in the header
    str_patterns = header[1:]  # Skip the 'name' column
    str_counts = [longest_str_repeat(dna_sequence, str_pattern) for str_pattern in str_patterns]

    # Find and print the matching profile
    match = find_matching_profile(header, data, str_counts)
    print(match)

if __name__ == "__main__":
    main()