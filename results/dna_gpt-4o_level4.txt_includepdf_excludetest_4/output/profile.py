import csv
import sys

def read_csv(file_path):
    """Reads the CSV file and returns the header and data."""
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames
        data = list(reader)
    return header, data

def read_dna_sequence(file_path):
    """Reads the DNA sequence from a text file."""
    with open(file_path, 'r') as file:
        sequence = file.read().strip()
    return sequence

def longest_match(sequence, subsequence):
    """Returns the length of the longest run of the subsequence in the sequence."""
    max_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while True:
            start = i + count * sub_len
            end = start + sub_len
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        max_run = max(max_run, count)

    return max_run

def find_matching_profile(profiles, str_counts):
    """Finds the matching profile based on the STR counts."""
    for profile in profiles:
        if all(int(profile[str_name]) == str_counts[str_name] for str_name in str_counts):
            return profile['name']
    return "No match"

def main():
    if len(sys.argv) != 3:
        print("Usage: python profile.py data.csv sequence.txt")
        return

    csv_file_path = sys.argv[1]
    sequence_file_path = sys.argv[2]

    header, profiles = read_csv(csv_file_path)
    sequence = read_dna_sequence(sequence_file_path)

    str_names = header[1:]  # Skip the 'name' column
    str_counts = {str_name: longest_match(sequence, str_name) for str_name in str_names}

    match = find_matching_profile(profiles, str_counts)
    print(match)

if __name__ == "__main__":
    main()